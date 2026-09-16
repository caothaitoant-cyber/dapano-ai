#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dpn — cong cu ghi/doc kho du lieu chung cua DAPANO GROUP.

Moi phong ban ghi du lieu QUA cong cu nay, khong sua tay file CSV.
Nho vay: ma so khong trung, cot khong lech, moi lan ghi deu co nhat ky.

    python3 cong-cu/dpn.py bang
    python3 cong-cu/dpn.py them khach-hang ho_ten="Nguyen Van A" sdt=09xx nhom=A
    python3 cong-cu/dpn.py xem khach-hang --loc nhom=A --so 10
    python3 cong-cu/dpn.py sua khach-hang KH-0001 buoc_8_2=5
    python3 cong-cu/dpn.py tong-quan
"""

import csv
import os
import re
import sys
from datetime import date, datetime

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KHO = os.path.join(GOC, "du-lieu")
NHAT_KY = os.path.join(KHO, "nhat-ky-ghi.log")

# ten bang -> (tien to ma, cot ma, danh sach cot, cot bat buoc)
BANG = {
    "khach-hang": (
        "KH", "ma_kh",
        ["ma_kh", "ho_ten", "sdt", "email", "nhom", "nguon", "tang_qua", "buoc_8_2",
         "ngan_sach", "thanh_pho", "phu_trach", "trang_thai", "ngay_tao", "ghi_chu"],
        ["ho_ten"],
    ),
    "tuong-tac": (
        "TT", "ma_tt",
        ["ma_tt", "ma_kh", "ngay", "kenh", "phong_ban", "noi_dung", "ket_qua", "hen_tiep_theo"],
        ["ma_kh", "noi_dung"],
    ),
    "toa-nha": (
        "TN", "ma_tn",
        ["ma_tn", "dia_chi", "thanh_pho", "dien_tich", "gia_chao", "gia_thue_thang",
         "noi_nam_1", "cap_rate", "dscr", "tran_gia_mua", "trang_thai", "ngay_tham_dinh", "nguon"],
        ["dia_chi"],
    ),
    "giao-dich": (
        "GD", "ma_gd",
        ["ma_gd", "ma_kh", "ma_tn", "loai", "gia_tri", "phi_dapano", "trang_thai",
         "ngay_ky", "ngay_thu", "ghi_chu"],
        ["ma_kh", "loai"],
    ),
    "chien-dich": (
        "CD", "ma_cd",
        ["ma_cd", "ten", "kenh", "tang_qua", "nhom_kh", "ngay_bat_dau", "ngay_ket_thuc",
         "chi_phi", "lead_thu_duoc", "trang_thai", "ghi_chu"],
        ["ten"],
    ),
    "cong-viec": (
        "CV", "ma_cv",
        ["ma_cv", "ngay_tao", "phong_ban", "tieu_de", "lien_quan", "uu_tien", "han",
         "trang_thai", "ket_qua"],
        ["phong_ban", "tieu_de"],
    ),
    "thu-chi": (
        "TC", "ma_tc",
        ["ma_tc", "ngay", "loai", "khoan_muc", "so_tien", "phong_ban", "lien_quan", "ghi_chu"],
        ["loai", "khoan_muc", "so_tien"],
    ),
}


def duong_dan(ten_bang):
    return os.path.join(KHO, ten_bang + ".csv")


def kiem_tra_bang(ten_bang):
    if ten_bang not in BANG:
        loi("Khong co bang '%s'. Cac bang hien co: %s" % (ten_bang, ", ".join(sorted(BANG))))


def loi(thong_diep):
    sys.stderr.write("LOI: %s\n" % thong_diep)
    sys.exit(1)


def doc(ten_bang):
    duong = duong_dan(ten_bang)
    if not os.path.exists(duong):
        return []
    with open(duong, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ghi_toan_bo(ten_bang, cac_dong):
    cot = BANG[ten_bang][2]
    duong = duong_dan(ten_bang)
    tam = duong + ".tam"
    with open(tam, "w", newline="", encoding="utf-8") as f:
        bo_ghi = csv.DictWriter(f, fieldnames=cot)
        bo_ghi.writeheader()
        for dong in cac_dong:
            bo_ghi.writerow({c: dong.get(c, "") for c in cot})
    os.replace(tam, duong)


def ghi_nhat_ky(hanh_dong, ten_bang, ma, chi_tiet):
    with open(NHAT_KY, "a", encoding="utf-8") as f:
        f.write("%s\t%s\t%s\t%s\t%s\n" % (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), hanh_dong, ten_bang, ma, chi_tiet))


def ma_tiep_theo(ten_bang):
    tien_to, cot_ma = BANG[ten_bang][0], BANG[ten_bang][1]
    lon_nhat = 0
    for dong in doc(ten_bang):
        ma = (dong.get(cot_ma) or "").strip()
        if ma.startswith(tien_to + "-"):
            duoi = ma.split("-", 1)[1]
            if duoi.isdigit():
                lon_nhat = max(lon_nhat, int(duoi))
    return "%s-%04d" % (tien_to, lon_nhat + 1)


def tach_cap(cac_tham_so):
    gia_tri = {}
    for tham_so in cac_tham_so:
        if "=" not in tham_so:
            loi("Tham so '%s' phai co dang cot=gia_tri" % tham_so)
        khoa, val = tham_so.split("=", 1)
        gia_tri[khoa.strip()] = val.strip()
    return gia_tri


def lenh_bang(_):
    print("KHO DU LIEU CHUNG — DAPANO GROUP\n")
    for ten in sorted(BANG):
        tien_to, cot_ma, cot, bat_buoc = BANG[ten]
        so_dong = len(doc(ten))
        print("  %-12s  %3d dong   ma: %s-0001" % (ten, so_dong, tien_to))
        print("      cot      : %s" % ", ".join(cot))
        print("      bat buoc : %s\n" % ", ".join(bat_buoc))


def lenh_them(cac_tham_so):
    if not cac_tham_so:
        loi("Cu phap: dpn.py them <bang> cot=gia_tri ...")
    ten_bang, cac_tham_so = cac_tham_so[0], cac_tham_so[1:]
    kiem_tra_bang(ten_bang)
    tien_to, cot_ma, cot, bat_buoc = BANG[ten_bang]
    gia_tri = tach_cap(cac_tham_so)

    la = [k for k in gia_tri if k not in cot]
    if la:
        loi("Bang '%s' khong co cot: %s\n     Cot hop le: %s"
            % (ten_bang, ", ".join(la), ", ".join(cot)))
    thieu = [k for k in bat_buoc if not gia_tri.get(k)]
    if thieu:
        loi("Thieu cot bat buoc: %s" % ", ".join(thieu))

    dong = {c: "" for c in cot}
    dong.update(gia_tri)
    dong[cot_ma] = ma_tiep_theo(ten_bang)
    hom_nay = date.today().isoformat()
    for cot_ngay in ("ngay_tao", "ngay"):
        if cot_ngay in cot and not dong.get(cot_ngay):
            dong[cot_ngay] = hom_nay
    if "trang_thai" in cot and not dong.get("trang_thai"):
        dong["trang_thai"] = "moi"

    cac_dong = doc(ten_bang)
    cac_dong.append(dong)
    ghi_toan_bo(ten_bang, cac_dong)
    ghi_nhat_ky("them", ten_bang, dong[cot_ma], "; ".join("%s=%s" % kv for kv in gia_tri.items()))
    print("Da them %s vao %s" % (dong[cot_ma], ten_bang))
    in_bang([dong], cot)


def lenh_sua(cac_tham_so):
    if len(cac_tham_so) < 3:
        loi("Cu phap: dpn.py sua <bang> <ma> cot=gia_tri ...")
    ten_bang, ma, cac_tham_so = cac_tham_so[0], cac_tham_so[1], cac_tham_so[2:]
    kiem_tra_bang(ten_bang)
    cot_ma, cot = BANG[ten_bang][1], BANG[ten_bang][2]
    gia_tri = tach_cap(cac_tham_so)
    la = [k for k in gia_tri if k not in cot or k == cot_ma]
    if la:
        loi("Khong sua duoc cot: %s" % ", ".join(la))

    cac_dong = doc(ten_bang)
    tim_thay = False
    for dong in cac_dong:
        if dong.get(cot_ma) == ma:
            dong.update(gia_tri)
            tim_thay = True
            break
    if not tim_thay:
        loi("Khong tim thay %s trong bang %s" % (ma, ten_bang))
    ghi_toan_bo(ten_bang, cac_dong)
    ghi_nhat_ky("sua", ten_bang, ma, "; ".join("%s=%s" % kv for kv in gia_tri.items()))
    print("Da cap nhat %s" % ma)


def lenh_xem(cac_tham_so):
    if not cac_tham_so:
        loi("Cu phap: dpn.py xem <bang> [--loc cot=gia_tri] [--so N]")
    ten_bang = cac_tham_so[0]
    kiem_tra_bang(ten_bang)
    cot = BANG[ten_bang][2]
    bo_loc, gioi_han, i = {}, 20, 1
    phan_con_lai = cac_tham_so[1:]
    while i <= len(phan_con_lai):
        tham_so = phan_con_lai[i - 1]
        if tham_so == "--loc" and i < len(phan_con_lai):
            bo_loc.update(tach_cap([phan_con_lai[i]]))
            i += 2
        elif tham_so == "--so" and i < len(phan_con_lai):
            gioi_han = int(phan_con_lai[i])
            i += 2
        else:
            loi("Khong hieu tham so '%s'" % tham_so)
    cac_dong = [d for d in doc(ten_bang)
                if all((d.get(k) or "").lower() == v.lower() for k, v in bo_loc.items())]
    print("%s — %d dong khop (hien %d)" % (ten_bang, len(cac_dong), min(gioi_han, len(cac_dong))))
    in_bang(cac_dong[-gioi_han:], cot)


def in_bang(cac_dong, cot):
    if not cac_dong:
        print("  (trong)")
        return
    hien = [c for c in cot if any((d.get(c) or "").strip() for d in cac_dong)]
    rong = {c: max(len(c), max(len((d.get(c) or "")) for d in cac_dong)) for c in hien}
    print("  " + "  ".join(c.ljust(rong[c]) for c in hien))
    print("  " + "  ".join("-" * rong[c] for c in hien))
    for d in cac_dong:
        print("  " + "  ".join((d.get(c) or "").ljust(rong[c]) for c in hien))


def so_tien(chuoi):
    """Doc so tien viet kieu Viet Nam (1.200.000) lan kieu quoc te (1,200,000.50)."""
    chuoi = (chuoi or "").strip().replace(" ", "")
    if not chuoi:
        return 0.0
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})+", chuoi):      # 1.200.000
        chuoi = chuoi.replace(".", "")
    elif re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", chuoi):  # 1,200,000.50
        chuoi = chuoi.replace(",", "")
    else:
        chuoi = chuoi.replace(",", ".")                  # 1,5 -> 1.5
    try:
        return float(chuoi)
    except ValueError:
        return 0.0


def lenh_tong_quan(_):
    khach = doc("khach-hang")
    viec = doc("cong-viec")
    gd = doc("giao-dich")
    tc = doc("thu-chi")
    hom_nay = date.today().isoformat()

    print("TONG QUAN DAPANO — %s\n" % hom_nay)
    print("KHACH HANG: %d" % len(khach))
    for nhan, cot in (("theo nhom", "nhom"), ("theo buoc 8+2", "buoc_8_2"), ("theo tang qua", "tang_qua")):
        dem = {}
        for d in khach:
            khoa = (d.get(cot) or "?").strip() or "?"
            dem[khoa] = dem.get(khoa, 0) + 1
        if dem:
            print("  %-16s %s" % (nhan + ":", "  ".join("%s=%d" % kv for kv in sorted(dem.items()))))

    dang_mo = [v for v in viec if (v.get("trang_thai") or "") not in ("xong", "huy")]
    tre_han = [v for v in dang_mo if (v.get("han") or "") and v["han"] < hom_nay]
    print("\nCONG VIEC: %d dang mo, %d TRE HAN" % (len(dang_mo), len(tre_han)))
    for v in tre_han[:10]:
        print("  [TRE] %s  %s  han %s  (%s)" % (v.get("ma_cv"), v.get("tieu_de"), v.get("han"), v.get("phong_ban")))

    da_ky = [g for g in gd if (g.get("ngay_ky") or "").strip()]
    chua_thu = [g for g in da_ky if not (g.get("ngay_thu") or "").strip()]
    print("\nGIAO DICH: %d tong, %d da ky, %d chua thu tien" % (len(gd), len(da_ky), len(chua_thu)))
    if chua_thu:
        print("  cong no phai thu: %s" % format(int(sum(so_tien(g.get("phi_dapano")) for g in chua_thu)), ","))

    thu = sum(so_tien(t.get("so_tien")) for t in tc if (t.get("loai") or "").lower().startswith("thu"))
    chi = sum(so_tien(t.get("so_tien")) for t in tc if (t.get("loai") or "").lower().startswith("chi"))
    print("\nTHU CHI: thu %s | chi %s | rong %s"
          % (format(int(thu), ","), format(int(chi), ","), format(int(thu - chi), ",")))
    print("\n(Con so tren la du lieu dang co trong du-lieu/. Thieu thi do chua ai ghi.)")


CAC_LENH = {
    "bang": lenh_bang,
    "them": lenh_them,
    "sua": lenh_sua,
    "xem": lenh_xem,
    "tong-quan": lenh_tong_quan,
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "giup"):
        print(__doc__)
        print("Cac lenh: %s" % ", ".join(CAC_LENH))
        return
    ten_lenh = sys.argv[1]
    if ten_lenh not in CAC_LENH:
        loi("Khong co lenh '%s'. Cac lenh: %s" % (ten_lenh, ", ".join(CAC_LENH)))
    CAC_LENH[ten_lenh](sys.argv[2:])


if __name__ == "__main__":
    main()
