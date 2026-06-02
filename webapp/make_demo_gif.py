"""Capture the webapp's 5-step flow as screenshots and stitch them into a GIF.

Usage (server must already be running on 127.0.0.1:8765):
    PYTHONUTF8=1 .venv/Scripts/python.exe webapp/make_demo_gif.py
Outputs:
    webapp/static/demo/step-*.png   (individual frames)
    webapp/static/demo.gif          (looping animation)
"""
from __future__ import annotations

import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8765/"
OUT_DIR = Path(__file__).resolve().parent / "static" / "demo"
GIF_PATH = Path(__file__).resolve().parent / "static" / "demo.gif"
VIEWPORT = {"width": 1280, "height": 860}

# (DOM id, caption) for each step container in index.html
STEPS = [
    ("step-upload", "① 上传研究数据 (.zip / 文件夹) + 你标注的 gold 科学问题"),
    ("step-agents", "② 勾选一个或多个 Agent，由它们阅读数据并各自提出科学问题"),
    ("step-judge", "③ 选择 Judge LLM，按 6 维加权 rubric(0–5 锚点)评分"),
    ("step-progress", "④ 实时进度：SSE 推送 agent 思考 / 候选问题 / judge 打分"),
    ("step-results", "⑤ 评测结果：排行榜 · 六维雷达 · 维度对比 · 时间分解"),
]


def _font(size: int) -> ImageFont.FreeTypeFont:
    for name in ("msyh.ttc", "msyhbd.ttc", "simhei.ttf", "C:/Windows/Fonts/msyh.ttc"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _annotate(png: Path, caption: str) -> None:
    """Draw a translucent caption bar at the bottom of the frame."""
    im = Image.open(png).convert("RGB")
    draw = ImageDraw.Draw(im, "RGBA")
    w, h = im.size
    bar_h = 56
    draw.rectangle([0, h - bar_h, w, h], fill=(20, 24, 33, 235))
    draw.rectangle([0, h - bar_h, 6, h], fill=(90, 140, 255, 255))
    font = _font(24)
    draw.text((24, h - bar_h + 14), caption, font=font, fill=(235, 240, 250))
    im.save(png)


def capture() -> list[Path]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frames: list[Path] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT, device_scale_factor=1)
        page.goto(URL, wait_until="networkidle")
        time.sleep(2)  # let API calls + charts settle
        for idx, (sid, caption) in enumerate(STEPS, 1):
            el = page.query_selector(f"#{sid}")
            if el is None:
                continue
            # bring the step's heading to the top so the frame leads with it
            page.evaluate(
                "id => document.getElementById(id)"
                ".scrollIntoView({block:'start'})",
                sid,
            )
            time.sleep(0.8)
            out = OUT_DIR / f"step-{idx}.png"
            page.screenshot(path=str(out))
            _annotate(out, caption)
            frames.append(out)
            print(f"captured {out.name}")
        browser.close()
    return frames


def make_gif(frames: list[Path]) -> None:
    imgs = [Image.open(f).convert("RGB") for f in frames]
    # normalise to the same size (first frame's size)
    w, h = imgs[0].size
    imgs = [im.resize((w, h)) if im.size != (w, h) else im for im in imgs]
    imgs[0].save(
        GIF_PATH,
        save_all=True,
        append_images=imgs[1:],
        duration=2200,   # ms per frame
        loop=0,
        optimize=True,
    )
    print(f"wrote {GIF_PATH} ({GIF_PATH.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    fr = capture()
    if not fr:
        raise SystemExit("no frames captured — is the server running on :8765?")
    make_gif(fr)
