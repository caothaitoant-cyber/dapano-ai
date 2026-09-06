# B3 · Đặc tả Máy Tính Dòng Tiền 10 Năm

File phát cho khách: [`may-tinh-dong-tien.xlsx`](./may-tinh-dong-tien.xlsx)
Script dựng lại file: [`dung-may-tinh.py`](./dung-may-tinh.py) · Script nghiệm thu: [`kiem-chung-may-tinh.py`](./kiem-chung-may-tinh.py)

> **Trạng thái: ĐÃ DỰNG XONG, CHỜ KIỂM CHỨNG BẰNG SỐ THẬT (A2).**
> Công thức đã được kiểm bằng mô hình độc lập. Còn thiếu bước cuối: chạy lại 5 hồ sơ đã giao dịch để chứng minh sai lệch dưới 5%.

---

## 1. Nguyên tắc thiết kế

**Mười bốn ô nhập ra một câu trả lời nên mua hay không.** Không làm mô hình 20 sheet cho oai — khách mở file trên điện thoại lúc đang ngồi cà phê với chủ nhà.

- Đơn vị thống nhất toàn file: **triệu đồng**. Toà 12 tỷ thì gõ `12000`.
- Chỉ ô nền vàng là gõ được. Toàn bộ ô công thức đã khoá.
- Không dùng hàm lạ (XLOOKUP, LET, IFS) để mở được bằng Google Sheet trên điện thoại.
- Ô để trống không làm vỡ file — mọi phép chia đều bọc trong `IF(mẫu số<=0, ...)`.

## 2. Bốn sheet

| Sheet | Vai trò |
|---|---|
| **1. Nhập liệu** | 14 ô khách gõ + 3 ô tự tính (tổng vốn, số tiền vay, tỷ lệ vay) |
| **2. Kết quả 10 năm** | Khối tóm tắt 9 dòng + bảng 10 năm × 14 cột |
| **3. Ba kịch bản** | Thận trọng / Cơ sở / Kỳ vọng, mỗi kịch bản một bảng 10 năm, cuối là bảng so sánh |
| **4. Đọc kết quả** | Giải thích 5 chỉ số bằng tiếng người + ngưỡng đèn đỏ + 3 câu tự hỏi trước khi đặt cọc |

## 3. Bản đồ ô nhập liệu (Sheet 1)

| Ô | Nội dung | Đơn vị | Số mẫu |
|---|---|---|---:|
| B7 | Giá mua toà nhà | triệu | 12.000 |
| B8 | Thuế, phí, công chứng | triệu | 300 |
| B9 | Phí môi giới | triệu | 120 |
| B10 | Chi phí cải tạo | triệu | 800 |
| **B11** | *Tổng vốn đầu tư* `=SUM(B7:B10)` | triệu | 13.220 |
| B14 | Vốn tự có | triệu | 9.500 |
| **B15** | *Số tiền vay* `=MAX(0,B11-B14)` | triệu | 3.720 |
| **B16** | *Tỷ lệ vay* `=IF(B11<=0,0,B15/B11)` | % | 28% |
| B17 | Lãi suất năm đầu | %/năm | 8,5% |
| B18 | Lãi suất thả nổi các năm sau | %/năm | 11,5% |
| B19 | Kỳ hạn vay | năm | 20 |
| B22 | Giá thuê thu được mỗi tháng | triệu/tháng | 75 |
| B23 | Số tháng để trống mỗi năm | tháng | 1,0 |
| B24 | Chi phí vận hành mỗi tháng | triệu/tháng | 6 |
| B25 | Thuế cho thuê | % doanh thu | 10% |
| B28 | Tốc độ tăng giá thuê mỗi năm | %/năm | 4% |
| B29 | Tốc độ tăng chi phí mỗi năm | %/năm | 5% |

> Số mẫu là **số minh hoạ, không phải khuyến nghị**. Khách thay bằng số toà nhà đang nhắm.

## 4. Công thức lõi (Sheet 2, năm thứ *n*)

```
Doanh thu thuê   = giá thuê tháng × (12 − số tháng trống) × (1 + tăng giá thuê)^(n−1)
Chi phí vận hành = chi phí tháng × 12 × (1 + tăng chi phí)^(n−1)
Thuế cho thuê    = doanh thu × % thuế
NOI              = doanh thu − chi phí vận hành − thuế

Gốc phải trả/năm = IF(kỳ hạn ≤ 0, 0, số tiền vay / kỳ hạn)
Dư nợ đầu năm    = MAX(0, số tiền vay − gốc/năm × (n−1))
Trả gốc          = MIN(gốc/năm, dư nợ đầu năm)
Trả lãi          = (dư nợ đầu năm + dư nợ cuối năm) / 2 × lãi suất
                   (lãi suất = ưu đãi ở năm 1, thả nổi từ năm 2)
Tổng trả nợ      = trả gốc + trả lãi

Dòng tiền ròng   = NOI − tổng trả nợ
DSCR             = NOI / tổng trả nợ
Cap Rate         = NOI / giá mua   và   NOI / tổng vốn đầu tư
```

**Vì sao chọn cách trả nợ này:** gốc đều, lãi trên dư nợ bình quân — đúng cách các ngân hàng Việt Nam đang áp dụng cho vay mua bất động sản. Không dùng annuity (trả đều) vì thực tế ít ngân hàng trong nước áp dụng cho khoản vay tài sản.

## 5. Ba kịch bản (Sheet 3) — giả định lệch nhau ở đâu

| Điều chỉnh | Thận trọng | Cơ sở | Kỳ vọng |
|---|---:|---:|---:|
| Giá thuê lệch | −10% | 0 | +7% |
| Số tháng trống mỗi năm | nhập + 1,5 | như nhập | nhập − 0,5 |
| Lãi suất cộng thêm | +2,0% | 0 | −0,5% |
| Tăng giá thuê mỗi năm | nhập − 1% | như nhập | nhập + 1% |

Bốn dòng này để **ô vàng sửa được** — mỗi thị trường một khẩu vị rủi ro khác nhau.

## 6. Ngưỡng cảnh báo cài trong file

| Chỉ số | Đèn đỏ | Đèn vàng | Đèn xanh |
|---|---|---|---|
| DSCR năm 1 | dưới 1,20 | 1,20 – 1,50 | trên 1,50 |
| Dòng tiền ròng | âm quá 18 tháng | âm 12–18 tháng khi có cải tạo | dương từ năm 1 |
| Tỷ lệ vay | trên 70% | 50–70% | dưới 50% |

## 7. Nghiệm thu

Chạy: `python3 ke-hoach-tang-qua/tang-1/kiem-chung-may-tinh.py`

Script đọc **chính công thức trong file xlsx**, tự tính lại, rồi đối chiếu với một mô hình dựng độc lập.

| Tiêu chí | Trạng thái |
|---|---|
| Công thức 10 năm khớp mô hình độc lập | ✅ Đạt |
| Kịch bản Cơ sở khớp Sheet 2 | ✅ Đạt |
| Ba kịch bản xếp đúng thứ tự thận trọng < cơ sở < kỳ vọng | ✅ Đạt |
| Nhập ô rỗng không lỗi chia 0 | ✅ Đạt |
| Làm tròn khớp cách Excel làm tròn (0,5 đi ra xa số 0) | ✅ Đạt |
| Ô công thức đã khoá, chỉ ô vàng gõ được | ✅ Đạt |
| **Sai lệch dưới 5% trên 5 hồ sơ thật (A2)** | ⬜ **Chờ số của kế toán** |
| Mở được bằng Google Sheet trên điện thoại | ⬜ Chờ thử trên máy thật |

**Kết quả với bộ số mẫu:** Cap Rate trên tổng vốn năm 1 là 5,07% · DSCR 1,36 (đèn vàng) · dòng tiền 14,7 triệu/tháng · luỹ kế 10 năm 3.049 triệu. Kịch bản thận trọng cho dòng tiền âm 5,2 triệu/tháng ở năm đầu — đúng tinh thần: nếu chỉ kịch bản kỳ vọng mới đẹp thì đang mua một hy vọng, không mua một dòng tiền.

## 8. Việc còn lại trước khi phát hành

1. **Điền A2** rồi chạy lại nghiệm thu, ghi kết quả vào bảng đối chiếu trong `00-du-lieu-goc/ho-so-kiem-chung.md`.
2. Tải lên Google Drive, tạo bản Google Sheet, mở thử trên điện thoại.
3. Đặt link tải cố định (không hết hạn) để nối vào luồng email C2.
4. Ghi tên người chịu trách nhiệm vào A3.

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
