# -*- coding: utf-8 -*-
"""Xuất Bản đồ Dòng Tiền ra PNG (A3 ngang) và PDF để in.

Cài một lần:  pip install playwright
Chạy:         python3 ke-hoach-tang-qua/tang-0/xuat-ban-do.py
Kết quả:      ban-do-dong-tien.png  ·  ban-do-dong-tien.pdf  (cùng thư mục)
"""
import asyncio, glob, os
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ban-do-dong-tien.html")
# A3 ngang = 420 × 297 mm; 1mm ≈ 3.7795 px ở 96 dpi
W, H = round(420 * 3.7795), round(297 * 3.7795)

async def main():
    async with async_playwright() as p:
        # Môi trường có sẵn Chromium riêng — dùng bản đó thay vì tải mới
        found = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
        browser = await p.chromium.launch(executable_path=found[0]) if found else await p.chromium.launch()
        page = await browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        await page.goto("file://" + SRC)
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(2000)
        await page.add_style_tag(content="body{padding:0!important;background:#fff!important}"
                                         ".sheet{margin:0!important;box-shadow:none!important}")
        el = await page.query_selector(".sheet")
        await el.screenshot(path=os.path.join(HERE, "ban-do-dong-tien.png"))
        await page.pdf(path=os.path.join(HERE, "ban-do-dong-tien.pdf"), width="420mm", height="297mm",
                       print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        await browser.close()
    print("Đã xuất PNG và PDF trong", HERE)

asyncio.run(main())
