# Trạng thái triển khai Thang Quà Dòng Tiền

Bản kiểm tra tiến độ: đối chiếu kế hoạch trong [`README.md`](./README.md) với những gì **thật sự đã có**.

Ngày kiểm: 06/09/2026 · Kết luận một dòng: **chiến lược đã xong, chưa có món quà nào ra hình để tặng được cho khách.**

Phân rã chi tiết từng hạng mục thành file cụ thể: [`bang-chi-tiet-hang-muc.md`](./bang-chi-tiet-hang-muc.md).

---

## 1. Đang có gì

| Hạng mục | Trạng thái |
|---|---|
| Kế hoạch thang quà 6 tầng, 5 lớp bán chéo, phễu 90 ngày | ✅ Xong (`README.md`) |
| Bản trình bày chuẩn nhận diện DAPANO để in/gửi nội bộ | ✅ Xong (`thang-qua-dong-tien.html`) |
| 3 kịch bản chuyển tầng (lời thoại) | ✅ Xong ở dạng bản thảo, **chưa diễn thử với sale** |
| Lịch content 8 bài / 4 tuần | ✅ Có tiêu đề & công thức, **chưa có bài viết nào** |

## 2. Đang mắc ở đâu — 10 chốt chặn

Xếp theo thứ tự phải làm. Chốt sau phụ thuộc chốt trước, làm ngược là hỏng.

### Nhóm A — Phải có số thật (chặn tất cả phần còn lại)

| # | Chốt chặn | Vì sao đang mắc | Cần ai / cần gì | Xong thì mở khoá được |
|---|---|---|---|---|
| **A1** | **Số Cap Rate & giá thuê thật** theo trục phố HN – HCM | Kế hoạch ghi "do đội thẩm định khảo sát" nhưng chưa có bảng số nào trong tay | Đội thẩm định xuất dữ liệu từ danh mục đang vận hành | Tầng 0, Tầng 1, Tầng 2 — cả ba đều ăn chung nguồn số này |
| **A2** | **5 hồ sơ giao dịch đã hoàn tất** để kiểm chứng công thức | Không có hồ sơ đối chiếu thì Máy tính dòng tiền chỉ là file Excel đoán mò | Kế toán / vận hành cung cấp giá mua, giá thuê, chi phí, dòng tiền thực tế | Máy tính dòng tiền được phép phát hành |
| **A3** | **Chốt tên chính thức + người chịu trách nhiệm từng tầng** | Chưa ai đứng tên tầng nào → không có ai bị hỏi khi trễ | Anh quyết trong 1 buổi họp 30 phút | Toàn bộ lộ trình 90 ngày có chủ |

### Nhóm B — Tài sản để tặng (chưa có món nào)

| # | Món quà | Trạng thái | Việc còn lại |
|---|---|---|---|
| **B1** | **Tầng 0 · Bản đồ Dòng Tiền HN – HCM** (A3, ảnh + PDF) | ❌ Chưa có | Cần A1 → viết nội dung → thiết kế theo brand DAPANO → xuất PNG + PDF |
| **B2** | **Tầng 1 · Cẩm nang "Toà Nhà Đầu Tiên"** (~40 trang) | ❌ Chưa có | Cần A1 + A2 để có ví dụ số thật → viết 7 bước → dàn trang PDF |
| **B3** | **Tầng 1 · Máy Tính Dòng Tiền 10 Năm** (Excel/Sheet) | ❌ Chưa có — **đây là món quan trọng nhất, cũng là món chưa động tới** | Dựng công thức NOI / Cap Rate / DSCR / dòng tiền ròng / điểm hoà vốn → kiểm chứng bằng A2 → khoá ô công thức → bản Excel + bản Google Sheet |
| **B4** | **Tầng 1 · Bộ 12 câu hỏi phải hỏi chủ nhà** | ❌ Chưa có | Viết 1 trang, lấy từ kinh nghiệm đội thẩm định |
| **B5** | **Tầng 2 · 12 câu hỏi sàng lọc + mẫu Báo cáo cá nhân 6–8 trang** | ❌ Chưa có | Viết bộ câu hỏi → dựng template báo cáo → chạy thử trên 2 khách cũ |
| **B6** | **Tầng 3 · Bộ 12 điểm kiểm pháp lý + Hợp đồng thuê mẫu** | ❌ Chưa có | Soạn → **bắt buộc qua rà soát pháp lý trước khi phát hành** |
| **B7** | **Tầng 4 · Kế hoạch nâng giá thuê 18 tháng (mẫu)** | ❌ Chưa có | Chuẩn hoá thành template để bàn giao cùng tài sản |

### Nhóm C — Đường ống dẫn khách (chưa dựng)

| # | Chốt chặn | Trạng thái | Việc còn lại |
|---|---|---|---|
| **C1** | **Landing page + form 3 trường** | ❌ Chưa có | Chưa chốt tên miền/nền tảng · chưa có trang · chưa có ảnh bìa |
| **C2** | **Luồng gửi file tự động trong 1 phút** | ❌ Chưa có | Email tự động + link tải + thư cảm ơn; phải tự đăng ký thử 3 lần |
| **C3** | **CRM + webhook nhận lead** | ❌ Chưa chọn công cụ | Chốt dùng CRM nào → dựng trường "nguồn" và "món quà đã tải" → quy định nhập trong 15 phút |
| **C4** | **Cổng thanh toán Tầng 3** (299.000đ / 1.000.000đ) | ❌ Chưa có | Chưa có cách thu tiền, chưa có quy chế hoàn 100% vào giao dịch bằng văn bản |
| **C5** | **8 bài content** | ❌ Mới có tiêu đề | Viết đủ 8 bài theo công thức đã gán · bài #4 (Before-After-Bridge) **phải có testimonial thật + giấy xin phép khách** |
| **C6** | **Ngân sách quảng cáo + người chạy ads** | ❌ Chưa chốt con số | Quyết ngân sách thử tháng đầu cho cả hai thành phố |

### Nhóm D — Vận hành & năng lực thật

| # | Chốt chặn | Trạng thái |
|---|---|---|
| **D1** | Đội thẩm định có kham nổi **30 hồ sơ/tháng** không? | ❓ Chưa xác nhận — nếu không kham nổi phải hạ số xuống, vì kế hoạch cấm khan hiếm giả |
| **D2** | Danh mục có đủ **≥ 6 toà sẵn sàng** cho field tour không? | ❓ Chưa kiểm — thiếu thì Tầng 3 mời khách đi xem cái gì |
| **D3** | Sale đã diễn thử 3 kịch bản chuyển tầng chưa? | ❌ Chưa — kịch bản mới nằm trên giấy |
| **D4** | Lịch cố định: 2 workshop/tháng, 1 field tour/tháng/thành phố | ❌ Chưa đặt ngày cụ thể |

## 3. Đường đi ngắn nhất để thông

Ba việc dưới đây làm xong là phễu chạy được ở mức tối thiểu (Tầng 0 → 1 → 2), ba tầng còn lại bổ sung sau:

1. **A1 + A2** — lấy số thật ra khỏi đầu đội thẩm định, đặt lên bảng. Không có bước này thì mọi thứ phía sau chỉ là văn bản đẹp.
2. **B3 · Máy Tính Dòng Tiền** — trái tim của Tầng 1. Dựng và kiểm chứng ngay sau khi có A2.
3. **C1 + C2 + C3** — landing page, gửi file tự động, CRM. Có quà mà không có ống dẫn thì quà nằm trong máy.

Chưa xong ba việc trên thì **chưa mở quảng cáo** — đúng như cảnh báo ở mục 9 của kế hoạch: sửa quà và tốc độ gọi trước, tăng ngân sách sau.

## 4. Việc em làm được ngay khi anh gật

- Dựng khung **Máy Tính Dòng Tiền 10 Năm** (B3) — chỉ cần anh đưa 3–5 hồ sơ thật để kiểm chứng công thức.
- Viết **12 câu hỏi hỏi chủ nhà** (B4) và **12 câu sàng lọc + mẫu Báo cáo cá nhân** (B5).
- Viết **8 bài content** (C5) theo đúng 8 công thức đã gán, trừ bài #4 phải chờ testimonial thật.
- Dựng **landing page + form** (C1) ở dạng trang tĩnh chuẩn nhận diện DAPANO.
- Soạn bản thảo **Cẩm nang "Toà Nhà Đầu Tiên"** (B2) khi đã có số của A1.

Việc **không** thể làm thay: A1, A2, D1, D2 (số và năng lực thật của đội), B6 (rà soát pháp lý), C3, C4 (chọn công cụ và tài khoản thanh toán).

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
