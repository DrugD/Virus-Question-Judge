from .base import AgentRunner, RunResult
from .codex_cli_agent import CodexCLIAgent, CodexGpt55High
from .claude_code_agent import (
    ClaudeCodeOpus47, ClaudeCodeSonnet46,
)
from .openai_chat_agent import OpenAIChatAgent  # legacy single-shot, kept importable
from .llm_tool_agent import (
    LLMToolAgent,
    GEMINI_PRO_TOOL, GEMINI_FLAS_TOOL,
    GLM_5_TOOL,
    DEEPSEEK_V4_PRO_TOOL,
    INTERN_S1_TOOL, INTERN_S1_PRO_TOOL, INTERN_S1_MINI_TOOL, INTERN_S2_TOOL,
)

# Public registry — id ↔ runner class.
#
# Routing policy (家家用自家脚手架，没 native CLI 的走通用 ReAct loop):
#   - Anthropic Claude  → ClaudeCode CLI (--model <claude-id>)
#   - OpenAI GPT        → Codex CLI       (-m <gpt-id>)
#   - Google Gemini     → generic LLMToolAgent (no local native CLI)
#   - Z.AI GLM          → generic LLMToolAgent
#   - DeepSeek          → generic LLMToolAgent (no native CLI)
#   - InternLM (浦语)   → generic LLMToolAgent · own endpoint chat.intern-ai.org.cn
REGISTRY: dict[str, type[AgentRunner]] = {
    # OpenAI — Codex CLI
    "gpt-5.5-high":           CodexGpt55High,
    # Anthropic — Claude Code CLI
    "claude-code-opus-4-7":   ClaudeCodeOpus47,
    "claude-code-sonnet-4-6": ClaudeCodeSonnet46,
    # Google — generic ReAct tool loop
    "gemini-3.1-pro":         GEMINI_PRO_TOOL,
    "gemini-2.5-flash":       GEMINI_FLAS_TOOL,
    # Z.AI — generic ReAct tool loop
    "glm-5":                  GLM_5_TOOL,
    # DeepSeek — generic ReAct tool loop (no native CLI)
    "deepseek-v4-pro":        DEEPSEEK_V4_PRO_TOOL,
    # InternLM (Shanghai AI Lab) — generic ReAct tool loop · own endpoint
    "intern-s1":              INTERN_S1_TOOL,
    "intern-s1-pro":          INTERN_S1_PRO_TOOL,
    "intern-s1-mini":         INTERN_S1_MINI_TOOL,
    "intern-s2-preview":      INTERN_S2_TOOL,
}

# Metadata for the UI: family + brief description.
AGENT_META: dict[str, dict[str, str]] = {
    "gpt-5.5-high":           {"family": "OpenAI",          "kind": "Codex CLI ReAct",       "desc": "GPT-5.5 (high effort) via Codex CLI"},
    "claude-code-opus-4-7":   {"family": "Anthropic",       "kind": "Claude Code CLI",       "desc": "Claude Opus 4.7 via Claude Code"},
    "claude-code-sonnet-4-6": {"family": "Anthropic",       "kind": "Claude Code CLI",       "desc": "Claude Sonnet 4.6 via Claude Code"},
    "gemini-3.1-pro":         {"family": "Google",          "kind": "tool-using ReAct loop", "desc": "Gemini 3.1 Pro preview + tool loop"},
    "gemini-2.5-flash":       {"family": "Google",          "kind": "tool-using ReAct loop", "desc": "Gemini 2.5 Flash + tool loop"},
    "glm-5":                  {"family": "Z.AI",            "kind": "tool-using ReAct loop", "desc": "GLM 5 + tool loop"},
    "deepseek-v4-pro":        {"family": "DeepSeek",        "kind": "tool-using ReAct loop", "desc": "DeepSeek V4 Pro + tool loop"},
    "intern-s1":              {"family": "InternLM (浦语)", "kind": "tool-using ReAct loop", "desc": "Intern-S1 · 32K · 多模态科学 · 需 INTERN_AI_KEY"},
    "intern-s1-pro":          {"family": "InternLM (浦语)", "kind": "tool-using ReAct loop", "desc": "Intern-S1 Pro · 256K · 科学推理+联网 · 需 INTERN_AI_KEY"},
    "intern-s1-mini":         {"family": "InternLM (浦语)", "kind": "tool-using ReAct loop", "desc": "Intern-S1 Mini · 32K · 轻量科学推理 · 需 INTERN_AI_KEY"},
    "intern-s2-preview":      {"family": "InternLM (浦语)", "kind": "tool-using ReAct loop", "desc": "Intern-S2 Preview · 256K · 35B-A3B · 需 INTERN_AI_KEY"},
}

__all__ = [
    "AgentRunner", "RunResult",
    "OpenAIChatAgent", "LLMToolAgent",
    "CodexCLIAgent", "CodexGpt55High",
    "ClaudeCodeOpus47", "ClaudeCodeSonnet46",
    "REGISTRY", "AGENT_META",
]
