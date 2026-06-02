"""Provider-agnostic judge-LLM wrapper.

Supports OpenAI-compatible chat APIs (OpenAI, DashScope/Qwen via the OpenAI SDK,
DeepSeek, etc.) and Anthropic. The judge always returns strict JSON; we parse
the first JSON object out of the response.
"""

from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass
from typing import Any


@dataclass
class JudgeConfig:
    provider: str               # "openai" | "anthropic" | "dashscope"
    model: str
    api_key_env: str            # name of the env var holding the key
    base_url: str | None = None # for OpenAI-compatible endpoints
    temperature: float | None = 0.0  # set to None to omit (e.g. Bedrock Opus 4.7 rejects it)
    max_tokens: int = 1024
    timeout: int = 120
    max_retries: int = 2


class JudgeLLM:
    """Thin client used by every rubric-dimension metric."""

    def __init__(self, cfg: JudgeConfig):
        self.cfg = cfg
        self._client = self._build_client()

    def _build_client(self):
        prov = self.cfg.provider
        key = os.environ.get(self.cfg.api_key_env)
        if not key:
            raise RuntimeError(
                f"Judge LLM env var {self.cfg.api_key_env} is not set."
            )

        if prov in ("openai", "dashscope"):
            from openai import OpenAI

            return OpenAI(api_key=key, base_url=self.cfg.base_url)
        if prov == "anthropic":
            from anthropic import Anthropic

            return Anthropic(api_key=key)
        raise ValueError(f"Unknown judge provider: {prov}")

    def chat_json(self, system: str, user: str) -> dict[str, Any]:
        """Run the judge once and return parsed JSON.

        Retries on transient errors (gateway timeouts, empty responses from
        Bedrock-hosted Claude under burst, etc). Uses linear backoff with
        slightly larger steps when the failure was an empty body — that's
        the Bedrock per-key throttle signature, and it usually clears in
        ~10s.
        """
        last_err: Exception | None = None
        budget = max(self.cfg.max_retries, 4)  # ensure at least 5 total attempts
        for attempt in range(budget + 1):
            try:
                raw = self._chat_raw(system, user)
                if not raw or not raw.strip():
                    # empty body — Bedrock throttle. Treat as retryable.
                    raise ValueError("empty judge response (likely Bedrock throttle)")
                return self._extract_json(raw)
            except Exception as e:
                last_err = e
                if attempt < budget:
                    is_throttle = isinstance(e, ValueError) and "empty" in str(e).lower()
                    delay = (8.0 if is_throttle else 1.5) * (attempt + 1)
                    time.sleep(delay)
                    continue
                raise
        raise last_err  # pragma: no cover

    def _chat_raw(self, system: str, user: str) -> str:
        prov = self.cfg.provider
        if prov in ("openai", "dashscope"):
            kwargs = dict(
                model=self.cfg.model,
                max_tokens=self.cfg.max_tokens,
                timeout=self.cfg.timeout,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
            # Some Bedrock-hosted models (e.g. Claude Opus 4.7) reject the
            # `temperature` field with a 400 ValidationException. Omit when None.
            if self.cfg.temperature is not None:
                kwargs["temperature"] = self.cfg.temperature
            # `response_format={"type":"json_object"}` is OpenAI-specific.
            # When Claude models are routed via the new-api gateway's
            # OpenAI-compat shim, the field either silently produces empty
            # output or 400s. The judge prompt already instructs JSON
            # output, and `_extract_json` regex-falls-back, so we just skip
            # the param for Claude models.
            model_lc = (self.cfg.model or "").lower()
            if not model_lc.startswith(("claude-", "anthropic")):
                kwargs["response_format"] = {"type": "json_object"}
            resp = self._client.chat.completions.create(**kwargs)
            return resp.choices[0].message.content or ""
        if prov == "anthropic":
            kwargs = dict(
                model=self.cfg.model,
                max_tokens=self.cfg.max_tokens,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            if self.cfg.temperature is not None:
                kwargs["temperature"] = self.cfg.temperature
            resp = self._client.messages.create(**kwargs)
            return "".join(b.text for b in resp.content if b.type == "text")
        raise ValueError(prov)

    @staticmethod
    def _extract_json(text: str) -> dict[str, Any]:
        text = text.strip()
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
        m = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not m:
            raise ValueError(f"Judge did not return JSON: {text[:300]}")
        return json.loads(m.group(0))
