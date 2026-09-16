# QUY TRÌNH LIÊN PHÒNG BAN

Phòng ban làm gì bên trong phòng mình đã ghi ở `.claude/agents/`. File này chỉ nói một điều:
**việc đi từ phòng này sang phòng kia như thế nào.** Đây là chỗ doanh nghiệp hay đứt gãy nhất.

## Luật bàn giao chung

Mọi lần chuyển việc phải kèm đủ **5 thứ**, thiếu một thứ thì phòng nhận có quyền trả lại:

1. **Mã** — `KH-xxxx` / `TN-xxxx` / `GD-xxxx`
2. **Đang ở đâu** — bước mấy của 8+2, tầng quà mấy, trạng thái gì
3. **Đã hứa gì** — nguyên văn, kể cả lời hứa miệng
4. **Cần gì tiếp** — việc cụ thể, không phải "nhờ xem giúp"
5. **Hạn** — ngày cụ thể

Bàn giao được ghi bằng một dòng trong `cong-viec.csv`, không bàn giao miệng.

---

## Luồng 1 · Từ người lạ tới hợp đồng

```
P2 Marketing ──quà Tầng 0-1──► lead mới
     │ ghi khach-hang.csv, gắn nguồn = mã chiến dịch
     ▼ (trong 24 giờ)
P1 Kinh doanh ──Bước 1→2→3→4──► khách nói ra con số thật
     │
     ├──► P3 Thẩm định  : Báo cáo Sức Khoẻ Dòng Tiền (Tầng 2, bước +1)
     │         │ trả báo cáo trong ‹điền› ngày
     │         ▼
     ├──► P1 Bước 5 (trình bày) → Bước 6 (chốt, giờ mới báo giá)
     │
     ├──► P3 Thẩm định  : định giá toà nhà cụ thể → trần giá mua
     ├──► P6 Pháp lý    : checklist 12 mục + rà hợp đồng
     │         │ một mục đỏ → DỪNG, báo anh Toàn
     ▼
ANH TOÀN ký ──► P5 Tài chính (ghi giao dịch, theo dõi thu)
              └► P4 Vận hành (nhịp chăm sóc sau ký)
                      │ tháng 12
                      ▼
                 P1 Bước +2: xin lời giới thiệu → quay lại đầu luồng
```

**Điểm đứt gãy hay gặp:** lead về mà quá 24 giờ chưa ai gọi. P0 soi chỗ này mỗi buổi giao ban.

---

## Luồng 2 · Khách hỏi về một toà nhà cụ thể

| Bước | Phòng | Việc | Hạn |
|---|---|---|---|
| 1 | P1 | Lấy đủ: địa chỉ, giá chào, giá thuê **thật**, diện tích, pháp lý sơ bộ | ngay trong buổi nói chuyện |
| 2 | P3 | Chạy 8 bước định giá → 3 kịch bản → trần giá mua | ‹điền› ngày |
| 3 | P6 | Checklist 12 mục pháp lý (chạy **song song** với bước 2) | ‹điền› ngày |
| 4 | P0 | Gộp hai kết quả, trình anh Toàn duyệt trần giá | 1 ngày |
| 5 | P1 | Trình bày cho khách bằng ngôn ngữ khách, không đọc số khô | |

**Cấm:** P1 tự nói trần giá trước khi có bước 4.

---

## Luồng 3 · Sau khi khách ký

```
P5 Tài chính   : ghi giao-dich.csv, theo dõi ngày thu, tính hoa hồng
P6 Pháp lý     : lưu bản hợp đồng cuối, liệt kê mọi cam kết thành checklist
P4 Vận hành    : nhận checklist cam kết → biến thành nhịp chăm sóc ngày 1 / 7 / tháng 1 / 6 / 12
P8 Dữ liệu     : đối chiếu dòng tiền thật vs. dự phóng của P3 mỗi tháng
```
**Dòng tiền thật lệch dự phóng quá ‹điền›% → P8 báo P0 → P0 báo anh Toàn trong 24 giờ.**
Đây là cơ chế giữ cho P3 không bao giờ dám vẽ số đẹp.

---

## Luồng 4 · Khách nguội

```
P1 phát hiện > 14 ngày không tương tác
   └► P4 kích hoạt lại bằng giá trị (3 lần chạm)
        ├─ có phản hồi → trả về P1, tiếp đúng bước đang dở
        └─ không phản hồi → P2 nuôi bằng content, dừng gọi
```
Không ai được xoá khách. Chuyển `trang_thai=nguoi` và giữ nguyên lịch sử.

---

## Luồng 5 · Sự vụ khẩn (khách bức xúc, toà nhà có vấn đề, rủi ro pháp lý)

1. Phòng nào nhận tin đầu tiên → ghi `tuong-tac.csv` **ngay**, không chờ xử lý xong.
2. Báo P0 trong **2 giờ**.
3. P0 gọi đúng phòng chuyên môn + chuẩn bị 2 phương án cho anh Toàn.
4. Phản hồi khách trong **48 giờ**, kể cả khi chưa xử lý xong.
5. Xong việc → ghi `05-nhat-ky-quyet-dinh.md`: chuyện gì, xử lý sao, sửa gì để không lặp lại.

---

## Bảng tra nhanh: việc này ai cầm?

| Tình huống | Phòng cầm chính | Phòng hỗ trợ |
|---|---|---|
| Lead mới về | P1 | P2 |
| Khách hỏi giá ở phút đầu | P1 | — |
| "Căn này mua được không?" | P3 | P6 |
| Khách chê đắt | P1 | P3 (đưa số chứng minh) |
| Hợp đồng bên bán gửi sang | P6 | P5 |
| Khách thuê chậm trả | P4 | P5 |
| Chi phí quảng cáo tăng | P2 | P5, P8 |
| Sale mới không chốt được | P7 | P1 |
| Anh Toàn hỏi "tháng này thế nào" | P8 | P5 |
| Không biết ai cầm | **P0** | — |
