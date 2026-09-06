# -*- coding: utf-8 -*-
"""Xuất bộ 12 câu hỏi phải hỏi chủ nhà ra PDF A4 (in hai mặt một tờ).

Cài một lần:  pip install playwright
Chạy:         python3 ke-hoach-tang-qua/tang-1/xuat-12-cau.py
Kết quả:      12-cau-hoi-chu-nha.pdf
"""
import asyncio, glob, os, sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "12-cau-hoi-chu-nha.html")
ANH = "--anh" in sys.argv   # thêm --anh để xuất kèm ảnh PNG từng trang (để soát bố cục)

async def main():
    async with async_playwright() as p:
        found = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
        browser = await p.chromium.launch(executable_path=found[0]) if found else await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 794, "height": 1123})
        await page.goto("file://" + SRC)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2500)
        so_trang = await page.evaluate("document.querySelectorAll('div.page').length")
        await page.pdf(path=os.path.join(HERE, "12-cau-hoi-chu-nha.pdf"), format="A4",
                       print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        if ANH:
            os.makedirs(os.path.join(HERE, "anh-soat"), exist_ok=True)
            for i, el in enumerate(await page.query_selector_all("div.page"), 1):
                await el.screenshot(path=os.path.join(HERE, "anh-soat", f"trang-{i:02d}.png"))
        await browser.close()
    print(f"Đã xuất PDF {so_trang} trang trong {HERE}")

asyncio.run(main())
