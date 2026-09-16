---
description: Dựng một chiến dịch marketing từ mục tiêu tới lịch đăng
argument-hint: "<mục tiêu> <nhóm khách A/B/C> <tầng quà> <kênh> <ngân sách>"
---

Dựng chiến dịch: $ARGUMENTS

Giao cho sub-agent `p2-marketing`, làm theo đúng thứ tự:

1. **Chốt ba lớp** trước khi viết chữ nào: đúng người (A/B/C) — đúng đau — đúng lợi ích.
2. **Chốt lối ra**: chiến dịch này kéo khách lên **tầng quà nào**? Chỉ một tầng.
3. **Ghi chiến dịch vào kho**:
   ```bash
   python3 cong-cu/dpn.py them chien-dich ten="…" kenh=… tang_qua=… nhom_kh=… \
     ngay_bat_dau=… ngay_ket_thuc=… chi_phi=0 trang_thai=nhap
   ```
4. **Sản xuất nội dung** bằng đúng skill cho từng định dạng
   (`compass-content-agent`, `letter-style-sales`, `video-marketing-28days`, `rem-bni-20s`).
   Mọi ấn phẩm hình ảnh/PDF/landing page chạy qua `dapano-brand`.
5. **Lịch đăng**: ngày nào, kênh nào, bài nào, ai bấm nút.
6. **Cách đo**: chỉ số nào tính là thắng, ngưỡng nào thì dừng đổ tiền.

Trả về gói hoàn chỉnh ở trạng thái **sẵn sàng đăng** và dừng lại:
đăng ra kênh công khai là việc anh Toàn bấm nút, không phải việc của phòng ban.
