---
description: Chạy quy trình định giá 8 bước cho một toà nhà và ra trần giá mua
argument-hint: "<địa chỉ> <giá chào> <giá thuê/tháng> <diện tích> [khách liên quan]"
---

Định giá tài sản: $ARGUMENTS

1. Giao cho sub-agent `p3-tham-dinh`, bắt buộc dùng skill `bds-cashflow-valuation`,
   chạy **đủ 8 bước**, xuất **đủ 8 phần**.
2. Trước khi tính, đối chiếu checklist dữ liệu đầu vào trong `.claude/agents/p3-tham-dinh.md`.
   **Thiếu giá chào hoặc giá thuê thật → dừng và hỏi anh Toàn, không tự giả định.**
3. Song song, giao `p6-phap-ly` chạy checklist 12 mục pháp lý cho địa chỉ này.
4. Kết quả ghi vào kho:
   ```bash
   python3 cong-cu/dpn.py them toa-nha dia_chi="…" thanh_pho=… gia_chao=… gia_thue_thang=… \
     noi_nam_1=… cap_rate=… dscr=… tran_gia_mua=… trang_thai=da-tham-dinh ngay_tham_dinh=<hôm nay>
   ```
5. Lưu báo cáo vào `bao-cao/<ngày>-P3-<địa-chỉ-rút-gọn>.md`.

Kết thúc bằng **một câu khuyến nghị dứt khoát**: mua ở mức nào, hay từ chối — kèm lý do bằng số.
Nhắc rõ: trần giá mua chỉ được gửi khách sau khi anh Toàn duyệt.
