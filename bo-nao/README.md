# BỘ NÃO CHUNG — DAPANO GROUP

Đây là **trí nhớ dài hạn duy nhất** của toàn công ty. Mọi phòng ban (sub-agent) đều đọc từ đây
và chỉ được ghi vào đây theo quy tắc ở `03-quy-tac-vang.md`.

> Nguyên tắc sống còn: **Một sự thật — một chỗ chứa.**
> Nếu một con số xuất hiện ở hai file khác nhau mà lệch nhau, hệ thống coi như hỏng.

## Bản đồ bộ não

| File | Chứa gì | Ai được sửa |
|---|---|---|
| [`00-ho-so-cong-ty.md`](./00-ho-so-cong-ty.md) | Công ty là ai, làm gì, cấu trúc phòng ban, mục tiêu năm | Anh Toàn (chủ tịch) |
| [`01-chan-dung-khach-hang.md`](./01-chan-dung-khach-hang.md) | 3 nhóm khách, nỗi đau, ngôn ngữ khách dùng | Marketing + Kinh doanh (đề xuất) |
| [`02-san-pham-va-gia.md`](./02-san-pham-va-gia.md) | Danh mục sản phẩm/dịch vụ, bảng giá, điều kiện | Anh Toàn duyệt, Tài chính ghi |
| [`03-quy-tac-vang.md`](./03-quy-tac-vang.md) | Luật bất di bất dịch của mọi phòng ban | Chỉ anh Toàn |
| [`04-tu-dien-chi-so.md`](./04-tu-dien-chi-so.md) | Định nghĩa KPI, công thức tính, ngưỡng cảnh báo | Dữ liệu & Báo cáo |
| [`05-nhat-ky-quyet-dinh.md`](./05-nhat-ky-quyet-dinh.md) | Mọi quyết định lớn + lý do + ngày | Điều phối ghi, không được xoá |
| [`06-tai-khoan-va-phan-quyen.md`](./06-tai-khoan-va-phan-quyen.md) | Quy tắc dùng chung 1 tài khoản an toàn | Anh Toàn |

## Cách nạp bộ não

- **Luôn tự động:** `CLAUDE.md` ở gốc repo được nạp vào mọi phiên làm việc.
- **Theo nhu cầu:** mỗi phòng ban tự đọc thêm file trong `bo-nao/` mà công việc của mình cần
  (đã ghi rõ trong file định nghĩa phòng ban ở `.claude/agents/`).

## Dấu `‹…›` nghĩa là gì

Chỗ nào còn `‹điền …›` là chỗ em chưa có số liệu thật của công ty — anh điền vào đó trước khi
chạy thật. Hệ thống được thiết kế để **không bịa số**: phòng ban nào gặp `‹điền …›` phải hỏi lại
anh chứ không được tự đoán.
