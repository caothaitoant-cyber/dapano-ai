# -*- coding: utf-8 -*-
"""Sinh ba email HTML của luồng gửi quà Tầng 1.

Chạy:    python3 ke-hoach-tang-qua/phieu-dan/tao-email.py
Kết quả: phieu-dan/email-1-gui-qua.html · email-2-huong-dan.html · email-3-moi-tang-2.html

Viết theo lối bảng + CSS nội tuyến để chạy được trên Outlook, Gmail, Apple Mail.
KHÔNG dùng webfont: phần lớn ứng dụng mail chặn. Dùng chồng font hệ thống,
giữ đúng bảng màu DAPANO. Nội dung lời văn gốc: luong-email-tu-dong.md
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
INDIGO, MAGENTA, GOLD, GOLDL = "#21135F", "#5E067C", "#D4A856", "#F0E0BA"
CREAM, SOFT, TEXT, MUTE, LIGHT = "#FAF7FC", "#F5F1F8", "#1A0F4A", "#6B5E85", "#E8E4F0"
FONT = "'Segoe UI',Roboto,'Helvetica Neue',Arial,'Noto Sans',sans-serif"

def nut(link, chu, phu=False):
    bg = f"background-color:{INDIGO};color:#ffffff" if phu else f"background-color:{GOLD};color:#2A1A05"
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:14px 0">'
            f'<tr><td align="center" style="{bg};border-radius:40px">'
            f'<a href="{link}" style="display:inline-block;padding:14px 28px;font-family:{FONT};font-size:16px;'
            f'font-weight:700;text-decoration:none;{bg.split(";")[1]}">{chu}</a></td></tr></table>')

def khung(tieu_de, eyebrow, than, preheader):
    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{tieu_de}</title></head>
<body style="margin:0;padding:0;background-color:{SOFT};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{SOFT};padding:22px 12px">
<tr><td align="center">
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:100%;background-color:#ffffff;border-radius:14px;overflow:hidden">
    <tr><td style="background-color:{INDIGO};padding:22px 28px">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
        <td style="font-family:{FONT};font-size:15px;font-weight:800;color:#ffffff;letter-spacing:3px">DAPANO GROUP</td>
        <td align="right" style="font-family:{FONT};font-size:10px;color:rgba(255,255,255,.65);letter-spacing:3px;text-transform:uppercase">Think Kind!</td>
      </tr></table>
      <div style="font-family:{FONT};font-size:10px;color:{GOLDL};letter-spacing:3.5px;text-transform:uppercase;font-weight:700;margin-top:16px">{eyebrow}</div>
      <div style="font-family:Georgia,'Times New Roman',serif;font-size:25px;color:#ffffff;line-height:1.22;margin-top:6px">{tieu_de}</div>
    </td></tr>
    <tr><td style="padding:26px 28px 22px;font-family:{FONT};font-size:15.5px;color:{TEXT};line-height:1.65">{than}</td></tr>
    <tr><td style="background-color:{CREAM};padding:18px 28px;border-top:1px solid {LIGHT};font-family:{FONT};font-size:12px;color:{MUTE};line-height:1.6">
      <div style="font-family:Georgia,serif;font-style:italic;font-size:15px;color:{MAGENTA};margin-bottom:8px">Cộng Hưởng Cùng Viên Mãn</div>
      DAPANO GROUP · {{{{website}}}}<br>
      Anh/chị nhận email này vì đã tải quà tặng của bên em. Nếu không muốn nhận thêm,
      <a href="{{{{link_huy}}}}" style="color:{MAGENTA}">bấm vào đây</a> là em dừng ngay ạ.
    </td></tr>
  </table>
  <div style="font-family:{FONT};font-size:11px;color:{MUTE};margin-top:14px;max-width:600px;line-height:1.55">
    Tài liệu trong bộ quà mang tính tham khảo, không phải lời khuyên đầu tư cá nhân hoá và không cam kết lợi nhuận.
  </div>
</td></tr></table></body></html>"""

def hop(noi_dung, mau=SOFT, vien=MAGENTA):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" '
            f'style="background-color:{mau};border-left:4px solid {vien};border-radius:8px;margin:14px 0">'
            f'<tr><td style="padding:14px 16px;font-family:{FONT};font-size:14.6px;color:{TEXT};line-height:1.6">{noi_dung}</td></tr></table>')

def mon(so, ten, mo_ta, link):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px">'
            f'<tr><td width="34" valign="top" style="font-family:Georgia,serif;font-size:22px;font-weight:bold;color:{MAGENTA};padding-top:2px">{so}</td>'
            f'<td style="font-family:{FONT};font-size:15px;color:{TEXT};line-height:1.5">'
            f'<b style="color:{INDIGO}">{ten}</b><br>'
            f'<span style="font-size:13.6px;color:{MUTE}">{mo_ta}</span><br>'
            f'<a href="{link}" style="color:{MAGENTA};font-weight:700;font-size:14px">Tải về →</a></td></tr></table>')

# ── EMAIL 1 ──────────────────────────────────────────────
e1 = khung(
 "Bộ Khởi Động Toà Nhà Đầu Tiên của anh/chị đây ạ",
 "Gửi ngay sau khi đăng ký",
 f"""<p style="margin:0 0 12px">Dạ em chào anh/chị <b>{{{{ho_ten}}}}</b>,</p>
<p style="margin:0 0 14px">Bộ quà của anh/chị đây ạ — em gửi kèm cả ba món:</p>
{mon(1,"Máy Tính Dòng Tiền 10 Năm","Excel và Google Sheet · nhập 14 ô, ra dòng tiền từng năm","{{link_may_tinh}}")}
{mon(2,"Cẩm nang “Toà Nhà Đầu Tiên”","20 trang PDF · bảy bước sở hữu một tài sản tự trả nợ cho mình","{{link_cam_nang}}")}
{mon(3,"Bộ 12 câu hỏi phải hỏi chủ nhà","Một tờ A4 in hai mặt, cầm theo khi đi xem nhà","{{link_12_cau}}")}
{hop("<b>Muốn dùng ngay?</b> Mở món số 1, chỉ gõ vào những ô màu vàng thôi ạ. Còn lại file tự tính.")}
<p style="margin:0 0 12px">Trong một hai ngày tới em xin phép gọi anh/chị một cuộc ngắn — chỉ để hỏi xem file có chỗ nào khó dùng không.
<b>Em không chào bán gì trong cuộc gọi đó ạ.</b></p>
<p style="margin:18px 0 0">Trân trọng,<br><b style="color:{INDIGO}">{{{{ten_chuyen_vien}}}}</b> · DAPANO GROUP</p>
<p style="margin:6px 0 0;font-family:Georgia,serif;font-style:italic;font-size:17px;color:{MAGENTA}">Nghĩ Thiện!</p>""",
 "Ba món trong bộ quà: máy tính dòng tiền, cẩm nang 20 trang và 12 câu hỏi chủ nhà.")

# ── EMAIL 2 ──────────────────────────────────────────────
e2 = khung(
 "Một phút để đọc kết quả trong file dòng tiền",
 "Gửi sau 48 giờ",
 f"""<p style="margin:0 0 12px">Dạ anh/chị <b>{{{{ho_ten}}}}</b>,</p>
<p style="margin:0 0 14px">Em gửi anh/chị cách đọc nhanh file Máy Tính Dòng Tiền ạ.</p>
{hop(f"<b style='color:{INDIGO}'>DSCR là con số quan trọng nhất.</b><br>Dưới 1,2 là đèn đỏ — chỉ cần toà nhà trống hai tháng là anh/chị phải bù tiền túi. Từ 1,5 trở lên thì tiền thuê gánh được nợ.")}
{hop(f"<b style='color:{INDIGO}'>Cột “Thận trọng” ở sheet 3 mới là cột đáng nhìn.</b><br>Nếu ở cột ấy dòng tiền vẫn dương thì toà nhà chịu được sóng gió. Nếu chỉ cột “Kỳ vọng” mới đẹp, nghĩa là mình đang mua một hy vọng chứ không mua một dòng tiền.", CREAM, GOLD)}
<p style="margin:0 0 12px">Anh/chị nhập thử một toà đang rao bán vào file rồi nhắn em con số DSCR ra bao nhiêu, em đọc giúp ạ.</p>
{nut("{{zalo}}","Nhắn Zalo cho em →", phu=True)}
<p style="margin:14px 0 0"><b style="color:{INDIGO}">{{{{ten_chuyen_vien}}}}</b> · DAPANO GROUP</p>""",
 "DSCR dưới 1,2 là đèn đỏ. Cột Thận trọng mới là cột đáng nhìn.")

# ── EMAIL 3 ──────────────────────────────────────────────
e3 = khung(
 "Anh/chị có muốn một bản phân tích riêng cho hồ sơ của mình không ạ?",
 "Gửi sau 5 ngày",
 f"""<p style="margin:0 0 12px">Dạ anh/chị <b>{{{{ho_ten}}}}</b>,</p>
<p style="margin:0 0 14px">File dòng tiền tính cho <b>một toà nhà</b>. Còn câu hỏi lớn hơn thường là:
<i style="color:{MAGENTA}">với vốn của mình, mình nên nhắm tài sản tầm bao nhiêu và vay được tới đâu?</i></p>
<p style="margin:0 0 12px">Mỗi tháng đội thẩm định bên em nhận một số hồ sơ để làm
<b style="color:{INDIGO}">Báo cáo Sức Khoẻ Dòng Tiền Cá Nhân</b>. Anh/chị trả lời 12 câu, bên em gửi lại bản phân tích riêng 6 trang:</p>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 14px">
<tr><td style="font-family:{FONT};font-size:14.8px;color:{TEXT};padding:4px 0">✓&nbsp; Khoảng giá tài sản phù hợp với vốn</td></tr>
<tr><td style="font-family:{FONT};font-size:14.8px;color:{TEXT};padding:4px 0">✓&nbsp; Cấu trúc vốn đề xuất, nên vay tới đâu</td></tr>
<tr><td style="font-family:{FONT};font-size:14.8px;color:{TEXT};padding:4px 0">✓&nbsp; Hai kịch bản dòng tiền mười năm</td></tr>
<tr><td style="font-family:{FONT};font-size:14.8px;color:{TEXT};padding:4px 0">✓&nbsp; Ba rủi ro riêng của hồ sơ anh/chị</td></tr>
</table>
{hop("Kèm 20 phút gọi giải thích. Miễn phí. Và trong cuộc gọi đó em <b>không giới thiệu bất kỳ toà nhà nào</b> — đó là nguyên tắc của bước này.")}
{nut("{{link_form_tang_2}}","Trả lời 12 câu →")}
<p style="margin:14px 0 0"><b style="color:{INDIGO}">{{{{ten_chuyen_vien}}}}</b> · DAPANO GROUP</p>""",
 "Trả lời 12 câu, nhận bản phân tích riêng 6 trang cho hồ sơ của anh/chị.")

for ten, noi_dung in [("email-1-gui-qua.html", e1), ("email-2-huong-dan.html", e2), ("email-3-moi-tang-2.html", e3)]:
    open(os.path.join(HERE, ten), "w", encoding="utf-8").write(noi_dung)
    print(f"  {ten} · {len(noi_dung)//1024} KB")
print("Đã sinh ba email. Điền các ô {{...}} bằng cau-hinh.json rồi dán vào công cụ gửi mail.")
