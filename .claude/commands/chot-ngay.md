---
description: Đóng sổ cuối ngày — ghi nốt dữ liệu, cập nhật việc, commit lại kho
---

Đóng sổ ngày hôm nay.

1. Rà lại phiên làm việc hôm nay: có khách nào đã chạm, tài sản nào đã xem, tiền nào đã thu/chi
   mà **chưa ghi vào `du-lieu/`** không? Ghi nốt bằng `cong-cu/dpn.py`.
2. Cập nhật trạng thái việc đã làm xong:
   ```bash
   python3 cong-cu/dpn.py sua cong-viec CV-00xx trang_thai=xong ket_qua="…"
   ```
3. Có quyết định lớn nào hôm nay không (đổi giá, dừng chiến dịch, từ chối khách)?
   → ghi vào `bo-nao/05-nhat-ky-quyet-dinh.md`.
4. Chạy `python3 cong-cu/dpn.py tong-quan` để xem trạng thái đóng ngày.
5. Commit lại kho dữ liệu:
   ```bash
   git add -A && git commit -m "Chot ngay <ngày>: <tóm tắt một dòng>"
   ```
   Hỏi anh Toàn trước khi `git push`.
6. Trả về 3 dòng: **hôm nay xong gì · mai phải làm gì trước tiên · đang chờ anh duyệt gì**.
