# -*- coding: utf-8 -*-
"""Tạo bộ font DAPANO nhúng sẵn (base64) để tài liệu in đúng nhận diện kể cả khi máy không có mạng.

Chạy:    python3 ke-hoach-tang-qua/assets/tao-font-dapano.py
Kết quả: ke-hoach-tang-qua/assets/fonts-dapano.css

Chỉ giữ hai subset cần cho tiếng Việt: vietnamese và latin.
Bốn font theo brandbook: Montserrat, Playfair Display, Dancing Script, Crimson Text.
"""
import base64, os, re, urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
URL = ("https://fonts.googleapis.com/css2"
       "?family=Montserrat:wght@400;500;600;700;800"
       "&family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700"
       "&family=Dancing+Script:wght@600;700"
       "&family=Crimson+Text:ital,wght@0,400;1,400"
       "&display=swap")
GIU = {"vietnamese", "latin"}  # bỏ latin-ext: tiếng Việt không cần
HERE = os.path.dirname(os.path.abspath(__file__))

def tai(url, ua=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA} if ua else {})
    return urllib.request.urlopen(req, timeout=60).read()

css = tai(URL).decode("utf-8")
khoi = re.findall(r"/\*\s*([a-z\-]+)\s*\*/\s*(@font-face\s*\{[^}]+\})", css)
ra, tong = [], 0
for subset, block in khoi:
    if subset not in GIU:
        continue
    m = re.search(r"url\((https://[^)]+\.woff2)\)", block)
    if not m:
        continue
    data = tai(m.group(1), ua=False)
    tong += len(data)
    b64 = base64.b64encode(data).decode()
    ra.append(block.replace(m.group(1), f"data:font/woff2;base64,{b64}"))

out = ("/* Bộ font DAPANO nhúng sẵn — Montserrat · Playfair Display · Dancing Script · Crimson Text.\n"
       "   Sinh tự động bởi tao-font-dapano.py. Đừng sửa tay. */\n" + "\n".join(ra) + "\n")
dest = os.path.join(HERE, "fonts-dapano.css")
open(dest, "w", encoding="utf-8").write(out)
print(f"Đã nhúng {len(ra)} font face · {tong//1024} KB woff2 · file CSS {os.path.getsize(dest)//1024} KB")
