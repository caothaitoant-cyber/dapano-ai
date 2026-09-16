---
description: Họp giao ban sáng — quét toàn hệ thống và ra 3–5 việc ưu tiên hôm nay
---

Chạy buổi giao ban sáng của DAPANO.

1. Chạy `python3 cong-cu/dpn.py tong-quan` và `python3 cong-cu/dpn.py xem cong-viec --so 50`.
2. Giao cho sub-agent `p0-dieu-phoi` chủ trì, trả lời đúng 4 câu hỏi giao ban trong file
   `.claude/agents/p0-dieu-phoi.md`.
3. Nếu có phòng ban nào đang có việc trễ hạn hoặc khách nóng chưa chạm, giao tiếp cho đúng
   sub-agent phòng đó xử lý ngay trong buổi giao ban (chạy song song).
4. Trả về đúng khối sau, không dài dòng:

```
GIAO BAN <ngày>

HÔM NAY LÀM 3–5 VIỆC NÀY
1. <việc> — <phòng> — <vì sao quan trọng nhất>
...

ĐANG CHỜ ANH TOÀN DUYỆT
• <…>

ĐỂ MAI
• <…>
```

5. Ghi các việc mới phát sinh vào `cong-viec.csv` bằng `cong-cu/dpn.py`.

Bối cảnh thêm từ anh Toàn (nếu có): $ARGUMENTS
