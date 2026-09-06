# Trạng thái triển khai Thang Quà Dòng Tiền

Đối chiếu kế hoạch trong [`README.md`](./README.md) với những gì **thật sự đã có trong tay**.
Phân rã chi tiết từng hạng mục: [`bang-chi-tiet-hang-muc.md`](./bang-chi-tiet-hang-muc.md).

**Cập nhật: 06/09/2026** · Kết luận một dòng: **toàn bộ phần dựng được đã dựng xong; phễu đang chờ đúng bốn thứ mà chỉ người trong công ty mới cấp được.**

---

## 1. Đã xong — dùng được ngay

| Mã | Hạng mục | File | Ghi chú |
|---|---|---|---|
| **B4** | Bộ 12 câu hỏi phải hỏi chủ nhà | [`tang-1/12-cau-hoi-chu-nha.md`](./tang-1/12-cau-hoi-chu-nha.md) | Đủ 12 câu kèm dấu hiệu cảnh giác. In một trang, phát được luôn |
| **B3** | Máy Tính Dòng Tiền 10 Năm | [`tang-1/may-tinh-dong-tien.xlsx`](./tang-1/may-tinh-dong-tien.xlsx) | 4 sheet · 14 ô nhập · khoá ô công thức · nghiệm thu tự động đạt |
| **B2** | Cẩm nang "Toà Nhà Đầu Tiên" | [`tang-1/cam-nang-toa-nha-dau-tien.pdf`](./tang-1/cam-nang-toa-nha-dau-tien.pdf) | 20 trang A4 chuẩn nhận diện, xuất PDF sẵn |
| **B5** | Bộ Tầng 2 | [`tang-2/`](./tang-2) | 12 câu sàng lọc + mẫu báo cáo 6 trang **tự tính số** từ hồ sơ khách |
| **C1** | Landing page Tầng 1 | [`phieu-dan/landing-page.html`](./phieu-dan/landing-page.html) | 7 khối, form 3 trường, chạy được sau khi điền 3 link cấu hình |
| **C2** | Luồng email tự động | [`phieu-dan/luong-email-tu-dong.md`](./phieu-dan/luong-email-tu-dong.md) | 3 email + 1 tin Zalo, nội dung viết sẵn |
| **C3** | Cấu hình CRM + webhook | [`phieu-dan/cau-hinh-crm.md`](./phieu-dan/cau-hinh-crm.md) | Mã Apps Script dán vào là chạy |
| **C5** | 8 bài content | [`content/`](./content) | 3 bài đăng được ngay, 5 bài chờ số thật |
| **D3** | Kịch bản chuyển tầng | [`van-hanh/kich-ban-chuyen-tang.md`](./van-hanh/kich-ban-chuyen-tang.md) | 3 kịch bản + 6 phản đối + checklist tự chấm |
| **D4** | Khung lịch workshop & field tour | [`van-hanh/lich-workshop-fieldtour.md`](./van-hanh/lich-workshop-fieldtour.md) | Kịch bản buổi đã có, chờ đặt ngày |
| **B7** | Kế hoạch nâng giá thuê 18 tháng | [`tang-4/`](./tang-4) | Template bàn giao cùng tài sản |
| — | Bộ font nhúng sẵn | [`assets/fonts-dapano.css`](./assets/fonts-dapano.css) | Tài liệu in đúng nhận diện kể cả khi máy không có mạng |

## 2. Đã dựng khung — chờ số hoặc chờ duyệt

| Mã | Hạng mục | Đang chờ gì | Ai cấp được |
|---|---|---|---|
| **B1** | Bản đồ Dòng Tiền Tầng 0 | 16 trục phố + 4 khoảng Cap Rate | Đội thẩm định (A1) |
| **A1** | Bảng Cap Rate HN–HCM | Số khảo sát thật | Đội thẩm định |
| **A2** | 5 hồ sơ kiểm chứng | Số thực thu, thực chi của 5 giao dịch đã xong | Kế toán + vận hành |
| **A3** | Phân công trách nhiệm | Một buổi họp 30 phút | Anh Toàn |
| **B6** | Bộ pháp lý Tầng 3 | **Chữ ký duyệt của pháp lý** | Luật sư / bộ phận pháp lý |
| **C4** | Quy chế thu & hoàn tiền | Duyệt của kế toán + pháp lý | Kế toán + pháp lý |
| **D1–D2** | Năng lực đội & danh mục tour | Đo thời gian thật một hồ sơ · đếm số toà sẵn sàng | Trưởng đội thẩm định |

## 3. Bốn thứ đang chặn cả phễu

Không có bốn thứ này thì mọi file ở trên chỉ chạy được một nửa.

| # | Đang thiếu | Chặn cái gì | Mất bao lâu để có |
|---|---|---|---|
| **1** | **Số Cap Rate & giá thuê thật** (A1) | Bản đồ Tầng 0 · bài content #1 · phần ví dụ trong cẩm nang | 2–3 ngày khảo sát |
| **2** | **5 hồ sơ đã giao dịch** (A2) | Chốt nghiệm thu Máy Tính Dòng Tiền · bài content #3 và #5 | 1 buổi trích sổ sách |
| **3** | **Ba link cấu hình** — webhook CRM, link tải bộ quà, Zalo chuyên viên | Landing page, luồng email, mọi CTA trong 8 bài content | 1 ngày |
| **4** | **Chữ ký pháp lý** cho bộ Tầng 3 và quy chế hoàn tiền | Toàn bộ Tầng 3: workshop, vé field tour, bài content #6 và #8 | Tuỳ luật sư |

## 4. Đường đi ngắn nhất để phễu chạy

**Tuần này** — họp 30 phút chốt A3 · đội thẩm định trích A1 và A2 · dựng 3 link cấu hình.
→ Xong ba việc này là **Tầng 0, 1, 2 chạy được thật**: có quà để tặng, có trang để nhận, có báo cáo để trả lại khách.

**Tuần sau** — đo D1–D2 và sửa hai con số 30 hồ sơ / 8 người theo thực tế · diễn thử D3 với cả đội · gửi bộ Tầng 3 cho pháp lý.

**Chỉ mở quảng cáo sau khi** tự đăng ký thử ba lần đều nhận được file trong dưới 60 giây, và sale đã diễn thử trọn ba kịch bản.

## 5. Luật cứng không được phá

- Không tăng ngân sách quảng cáo khi tỷ lệ **Tầng 1 → Tầng 2 dưới 10%**. Sửa quà và tốc độ gọi trước.
- Không đăng bài content nào còn ô `{{...}}` chưa điền.
- Không phát hành bộ pháp lý Tầng 3 khi chưa có chữ ký duyệt.
- Không công bố con số năng lực (30 hồ sơ, 8 người) khác với số đo được.
- Không bịa ví dụ, không bịa testimonial. Bài #5 khoá đăng cho tới khi có giấy xin phép khách.

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
