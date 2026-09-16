# HƯỚNG DẪN TRIỂN KHAI — 30 PHÚT ĐẦU TIÊN

Thưa anh Toàn,

Hệ thống đã dựng xong và chạy được ngay. Anh chỉ cần làm đúng ba việc dưới đây là bắt đầu
điều khiển được cả chín phòng ban bằng một tài khoản.

---

## Việc 1 — Nạp sự thật của công ty vào bộ não (20 phút, làm một lần)

Em đã dựng sẵn khung. Chỗ nào em chưa biết số thật thì em để dấu `‹điền …›` chứ **không bịa**.
Anh mở ba file này và điền vào:

| File | Điền gì | Vì sao quan trọng |
|---|---|---|
| `bo-nao/00-ho-so-cong-ty.md` | Mục tiêu năm, nhân sự thật phụ trách từng phòng | P0 dựa vào đây để chia việc |
| `bo-nao/02-san-pham-va-gia.md` | Gói tư vấn/môi giới/vận hành và mức phí | **Không phòng nào được báo giá khi bảng này còn trống** |
| `bo-nao/04-tu-dien-chi-so.md` | Ngưỡng Cap Rate tối thiểu, lead/tuần, chi phí/lead tối đa | P3 dùng để dám từ chối một toà nhà |

Cách nhanh nhất: anh nói với em bằng lời, em điền vào file cho anh.

## Việc 2 — Chạy thử một vòng (5 phút)

```bash
python3 cong-cu/dpn.py bang         # xem 7 bảng dữ liệu
python3 cong-cu/dpn.py tong-quan    # bảng điều khiển nhanh
```

Rồi thử ba lệnh nghiệp vụ:

```
/khach-moi   Chị Lan, 09xxxxxxxx, từ hội thảo BNI, đang gửi tiết kiệm 3 tỷ sắp đáo hạn
/giao-ban
/bao-cao-tuan
```

## Việc 3 — Đưa việc thật vào (làm dần)

Mỗi khách đang có, mỗi toà nhà đang xem, mỗi khoản thu chi — cứ nói với em bằng lời thường,
em ghi vào đúng bảng. Sau 2 tuần kho dữ liệu đủ dày là báo cáo bắt đầu có giá trị.

---

## Một ngày làm việc điển hình

| Lúc nào | Anh gõ | Chuyện gì xảy ra |
|---|---|---|
| Sáng | `/giao-ban` | P0 quét việc trễ, khách nóng, công nợ → đưa anh 3–5 việc |
| Có khách mới | `/khach-moi <thông tin>` | Ghi CRM, phân nhóm A/B/C, P1 soạn kịch bản chạm |
| Khách hỏi một toà nhà | `/dinh-gia <địa chỉ, giá, giá thuê>` | P3 chạy 8 bước, P6 rà pháp lý song song |
| Cần content | "viết cho anh post cho nhóm B" | P2 tự chọn đúng công thức và skill |
| Cuối ngày | `/chot-ngay` | Ghi nốt dữ liệu, cập nhật việc, commit |
| Cuối tuần | `/bao-cao-tuan` | P8 + P5 ra báo cáo, chỉ đúng chỗ phễu đang tắc |

Anh cũng có thể gọi thẳng một phòng: *"giao phòng thẩm định tính giúp anh căn này"* —
em sẽ chuyển đúng sub-agent.

---

## Dùng ở đâu

Cùng một tài khoản, cùng repo này, anh mở ở đâu cũng ra đúng bộ não:

- **Điện thoại / trình duyệt** — claude.ai/code, chọn repo `dapano-ai`. Hợp lúc đi đường.
- **Máy tính (Claude Code)** — `git clone` repo về rồi chạy trong thư mục đó. Hợp lúc làm sâu.
- **Ứng dụng desktop** — mở thư mục repo.

Điều kiện duy nhất: **luôn làm việc bên trong repo `dapano-ai`**. Ra ngoài repo là ra ngoài
bộ não — em sẽ không biết công ty đã hứa gì với khách.

---

## Khi có thêm người

Đọc `bo-nao/06-tai-khoan-va-phan-quyen.md`. Tóm tắt: người mới **không** được cấp tài khoản
riêng ngay. Hai tuần đầu làm qua anh, sau đó cấp quyền repo, cuối cùng mới cấp tài khoản —
và tài khoản mới vẫn trỏ về đúng repo này. Nhiều cái đầu làm việc, một trí nhớ duy nhất.

---

## Ba điều xin anh giữ giúp em

1. **Đừng sửa tay file CSV.** Luôn qua `cong-cu/dpn.py` — sửa tay là lệch cột, hỏng dữ liệu.
2. **Đừng bỏ `/chot-ngay`.** Việc không ghi lại thì tuần sau không ai nhớ đã hứa gì với khách.
3. **Chỗ nào còn `‹điền›` thì em sẽ hỏi chứ không đoán.** Anh thấy em hỏi nhiều ở tuần đầu
   là hệ thống đang chạy đúng.

Nghĩ Thiện!
