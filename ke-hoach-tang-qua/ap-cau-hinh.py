# -*- coding: utf-8 -*-
"""Điền cấu hình vào toàn bộ trang và bài content, xuất ra thư mục ban-phat-hanh/.

Chạy:    python3 ke-hoach-tang-qua/ap-cau-hinh.py
Kết quả: ke-hoach-tang-qua/ban-phat-hanh/... (bản đã điền, sẵn đăng)

File gốc trong repo LUÔN giữ nguyên ô {{...}} để lần sau còn điền lại được.
Script trả mã lỗi khác 0 nếu còn ô chưa điền — dùng được như một cửa chặn
trước khi đăng: còn ô trống thì chưa được đăng.
"""
import json, os, re, shutil, sys

GOC = os.path.dirname(os.path.abspath(__file__))
RA = os.path.join(GOC, "ban-phat-hanh")

NGUON = [
    "content/01-list-12-truc-pho.md", "content/02-pas-gui-tiet-kiem.md",
    "content/03-myth-mat-pho.md", "content/04-question-anh-dang-o-dau.md",
    "content/05-bab-anh-t-chu-xuong-go.md", "content/06-enemy-nghe-cua-em-la-doc-so.md",
    "content/07-story-toa-nha-thu-47.md", "content/08-direct-response-buoi-khao-sat.md",
    "phieu-dan/landing-page.html", "phieu-dan/form-tang-2.html", "phieu-dan/trang-tang-3.html",
    "phieu-dan/email-1-gui-qua.html", "phieu-dan/email-2-huong-dan.html", "phieu-dan/email-3-moi-tang-2.html",
    "tang-0/ban-do-dong-tien.html", "tang-1/12-cau-hoi-chu-nha.html",
]

# hằng số đặt sẵn trong các trang → khoá tương ứng trong cau-hinh.json
HANG_SO = {
    "DAN_URL_GOOGLE_APPS_SCRIPT_VAO_DAY": "webhook_url",
    "DAN_LINK_TAI_BO_QUA_VAO_DAY": "link_landing",
    "https://zalo.me/SO_ZALO_CHUYEN_VIEN": "zalo",
}

def phang(d, ra=None):
    """Gộp mọi nhóm trong cau-hinh.json thành một từ điển phẳng."""
    ra = {} if ra is None else ra
    for k, v in d.items():
        if k.startswith("_"):
            continue
        if isinstance(v, dict):
            phang(v, ra)
        else:
            ra[k] = v
    return ra

def main():
    cfg_path = os.path.join(GOC, "cau-hinh.json")
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    gia_tri = phang(cfg)
    giu = set(cfg.get("_giu_nguyen", {}).get("danh_sach", []))

    if os.path.isdir(RA):
        shutil.rmtree(RA)

    tong_thieu, xong, thieu_file = 0, [], []
    for rel in NGUON:
        src = os.path.join(GOC, rel)
        if not os.path.exists(src):
            print(f"  ✗ thiếu file nguồn: {rel}")
            continue
        s = open(src, encoding="utf-8").read()

        for hang, khoa in HANG_SO.items():
            if gia_tri.get(khoa):
                s = s.replace(hang, gia_tri[khoa])
        for khoa, val in gia_tri.items():
            if val:
                s = s.replace("{{" + khoa + "}}", str(val))

        con = [o for o in re.findall(r"\{\{([a-z0-9_]+)\}\}", s) if o not in giu]
        con_hang = [h for h in HANG_SO if h in s]

        dich = os.path.join(RA, rel)
        os.makedirs(os.path.dirname(dich), exist_ok=True)
        open(dich, "w", encoding="utf-8").write(s)

        if con or con_hang:
            tong_thieu += 1
            thieu_file.append((rel, sorted(set(con)) + con_hang))
        else:
            xong.append(rel)

    # bộ font đi kèm để trang trong ban-phat-hanh/ vẫn đúng nhận diện
    fonts = os.path.join(GOC, "assets", "fonts-dapano.css")
    if os.path.exists(fonts):
        os.makedirs(os.path.join(RA, "assets"), exist_ok=True)
        shutil.copy(fonts, os.path.join(RA, "assets", "fonts-dapano.css"))

    print(f"\n✅ ĐIỀN ĐỦ, ĐĂNG ĐƯỢC ({len(xong)} file)")
    for f in xong:
        print("   ·", f)
    if thieu_file:
        print(f"\n⛔ CÒN Ô TRỐNG — CHƯA ĐƯỢC ĐĂNG ({len(thieu_file)} file)")
        for f, o in thieu_file:
            print(f"   · {f}\n     thiếu: {', '.join(o)}")
    print(f"\nBản đã điền nằm trong: {os.path.relpath(RA, os.path.dirname(GOC))}")
    print("File gốc trong repo giữ nguyên ô {{...}} để lần sau điền lại.")
    return 1 if thieu_file else 0

if __name__ == "__main__":
    sys.exit(main())
