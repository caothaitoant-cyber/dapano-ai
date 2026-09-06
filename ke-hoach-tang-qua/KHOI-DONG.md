# 🚀 Khởi động Thang Quà Dòng Tiền — 7 ngày

Mọi thứ dựng được đã dựng xong. File này là **đường chạy**: mỗi ngày một việc, ai làm, xong thì kiểm thế nào.

> **Nguyên tắc:** không nhảy ngày. Ngày sau dùng kết quả của ngày trước.
> Cuối tuần thứ nhất, phễu Tầng 0 – 1 – 2 chạy thật với khách thật.

---

## Ngày 1 · Chốt người và tên — 30 phút

**Ai:** anh Toàn · **File:** [`00-du-lieu-goc/phan-cong-trach-nhiem.md`](./00-du-lieu-goc/phan-cong-trach-nhiem.md)

- [ ] Mỗi tầng ghi **đúng một** cái tên chịu trách nhiệm. Hai tên là không có tên nào.
- [ ] Chốt tên chính thức cho tám món quà (bảng "Chốt tên chính thức").
- [ ] Chốt ngân sách quảng cáo thử tháng đầu cho mỗi thành phố.
- [ ] Chốt ai cầm tài khoản quảng cáo và ai đối soát thanh toán.

**Xong khi:** bảng phân công không còn ô trống ở cột "Người chịu trách nhiệm".

---

## Ngày 2 · Lấy số thật ra khỏi đầu đội thẩm định

**Ai:** đội thẩm định + kế toán · **File:** [`cap-rate-hn-hcm.md`](./00-du-lieu-goc/cap-rate-hn-hcm.md) · [`ho-so-kiem-chung.md`](./00-du-lieu-goc/ho-so-kiem-chung.md)

- [ ] **A1** — điền tối thiểu 6 trục Hà Nội + 6 trục TP.HCM, mỗi trục ≥ 3 mẫu thật, có ngày khảo sát và độ tin cậy.
- [ ] **A1** — chốt 4 khoảng Cap Rate để tô màu bản đồ.
- [ ] **A2** — trích 5 hồ sơ đã giao dịch, đủ 8 trường, đã ẩn danh.

**Xong khi:** không dòng nào ghi "khoảng chừng"; mọi con số truy được về một hồ sơ hoặc một lần khảo sát có ngày tháng.

---

## Ngày 3 · Nghiệm thu Máy Tính Dòng Tiền bằng số thật

**Ai:** người phụ trách Tầng 1

```bash
python3 ke-hoach-tang-qua/tang-1/kiem-chung-may-tinh.py
```

- [ ] Nhập lần lượt 5 hồ sơ A2 vào [`may-tinh-dong-tien.xlsx`](./tang-1/may-tinh-dong-tien.xlsx), ghi kết quả vào bảng đối chiếu cuối file `ho-so-kiem-chung.md`.
- [ ] **Sai lệch dòng tiền ròng năm 1 phải dưới 5%** ở cả 5 hồ sơ. Vượt thì sửa công thức, **không sửa số thực tế**.
- [ ] Tải file lên Drive, tạo bản Google Sheet, mở thử trên điện thoại.
- [ ] Đặt link tải **cố định, không hết hạn** cho cả ba món quà.

**Xong khi:** bảng đối chiếu đủ 5 dòng "Đạt", và ba link tải mở được từ điện thoại người khác.

---

## Ngày 4 · Điền số vào bản đồ và bài content

**Ai:** người phụ trách Tầng 0 + người viết content

- [ ] Mở [`tang-0/ban-do-dong-tien.html`](./tang-0/ban-do-dong-tien.html), sửa khối `<script id="du-lieu">` bằng số A1.
- [ ] Xuất lại bản in: `python3 ke-hoach-tang-qua/tang-0/xuat-ban-do.py`
- [ ] Điền số A1 và số hồ sơ thật vào [`cau-hinh.json`](./cau-hinh.json) — nhóm `so_lieu_thi_truong_A1` và `ho_so_that_bai_3`.

**Xong khi:** bản đồ hiện "6/8 trục đã có số" trở lên ở cả hai thành phố, không còn ô "chờ số khảo sát" ở nhóm 1 và 2.

---

## Ngày 5 · Dựng đường ống dẫn khách

**Ai:** người phụ trách phễu · **File:** [`phieu-dan/cau-hinh-crm.md`](./phieu-dan/cau-hinh-crm.md)

- [ ] Tạo Google Sheet `Leads`, dán mã Apps Script, **Deploy → Web app → Anyone**, lấy URL.
- [ ] Điền [`cau-hinh.json`](./cau-hinh.json) — nhóm `he_thong` và `link_tai_lieu`.
- [ ] Chạy điền cấu hình:

```bash
python3 ke-hoach-tang-qua/ap-cau-hinh.py
```

- [ ] Đưa ba trang trong `ban-phat-hanh/phieu-dan/` lên hosting: landing page, form Tầng 2, trang Tầng 3.
- [ ] Dán ba email trong `ban-phat-hanh/phieu-dan/email-*.html` vào công cụ gửi mail, đặt lịch: ngay · 48 giờ · 5 ngày.

**Xong khi:** script `ap-cau-hinh.py` báo **ĐIỀN ĐỦ, ĐĂNG ĐƯỢC** cho cả ba trang và ba email.

---

## Ngày 6 · Luyện sale và đo năng lực thật

**Ai:** trưởng nhóm sale + đội thẩm định

- [ ] Diễn thử [`kich-ban-chuyen-tang.md`](./van-hanh/kich-ban-chuyen-tang.md): mỗi sale một lượt trọn 3 kịch bản + 6 phản đối. Một người đóng khách khó (hỏi giá ngay câu thứ hai, đòi cam kết lợi nhuận).
- [ ] **Ai để lộ giá sớm thì diễn lại từ đầu.** Chưa qua thì chưa nhận lead.
- [ ] Bấm giờ làm thử **một** Báo cáo cá nhân từ đầu đến cuối → điền [`nang-luc-doi-tham-dinh.md`](./van-hanh/nang-luc-doi-tham-dinh.md).
- [ ] Quy ra năng lực tháng. **Nếu khác 30 thì sửa con số 30** trong `cau-hinh.json` (`so_ho_so_thang`), form Tầng 2, email 3 và bài content #4.
- [ ] Đếm số toà sẵn sàng cho field tour. Dưới 6 toà thì **chưa mở bán vé Tầng 3**.

**Xong khi:** có một con số năng lực thật thay cho con số giả định, và mọi sale đã diễn thử xong.

---

## Ngày 7 · Chạy thử toàn tuyến rồi mới mở quảng cáo

**Ai:** người phụ trách phễu

**Tự đăng ký thử ba lần** bằng ba email khác nhau — Gmail, mail công ty, và một hộp thư mở trên điện thoại:

- [ ] Lần 1 · file về trong **dưới 60 giây**, không rơi vào Spam hay mục Quảng cáo
- [ ] Lần 2 · ba link tải đều mở được
- [ ] Lần 3 · lead hiện trong sheet `Leads` dưới 15 giây, giữ nguyên số 0 đầu số điện thoại, có đúng cột Nguồn và Quà đã tải
- [ ] Lead được phân cho đúng người, có nhật ký cuộc gọi đầu tiên
- [ ] Gửi thử form Tầng 2, kiểm 12 câu trả lời về đủ trong sheet
- [ ] Đăng **bài đầu tiên** — #7 Story (`content/07-story-toa-nha-thu-47.md`), là bài không cần số thị trường
- [ ] Mở quảng cáo **ngân sách nhỏ** ở một thành phố trước

**Xong khi:** ba lần thử đều trót lọt. Còn một lần lỗi thì sửa xong mới mở quảng cáo.

---

## Bảng đèn — chưa xanh thì chưa được làm

| Muốn làm việc này | Phải xanh trước |
|---|---|
| Phát Máy Tính Dòng Tiền cho khách | Nghiệm thu 5 hồ sơ A2 sai lệch dưới 5% |
| Đăng bài content #1 | A1 đã có số, `ap-cau-hinh.py` báo đăng được |
| Đăng bài content #3 | Ba ví dụ lấy từ hồ sơ thật đã ẩn danh |
| Đăng bài content #5 | **Testimonial thật + giấy xin phép khách bằng văn bản** |
| Đăng bài #6, #8 · mở trang Tầng 3 | Lịch có ngày thật · quy chế hoàn tiền đã được kế toán và pháp lý duyệt |
| Phát bộ pháp lý Tầng 3 | Luật sư đã ký duyệt hai file trong `tang-3/` |
| Công bố "30 hồ sơ/tháng", "8 chỗ" | Đã đo và con số công bố **đúng bằng** con số đo được |
| Tăng ngân sách quảng cáo | Tỷ lệ Tầng 1 → Tầng 2 **trên 10%** |

## Ba con số theo hằng tuần từ tuần thứ hai

**Chi phí mỗi lead Tầng 1** · **tỷ lệ Tầng 1 → 2** · **tỷ lệ Tầng 2 → 3**

Tầng 1 → 2 dưới 10% nghĩa là quà Tầng 1 đang hút sai người, hoặc sale gọi quá muộn. **Sửa quà và tốc độ gọi trước khi tăng tiền quảng cáo.**

## Lệnh hay dùng

```bash
python3 ke-hoach-tang-qua/ap-cau-hinh.py            # điền cấu hình, kiểm ô trống
python3 ke-hoach-tang-qua/tang-1/kiem-chung-may-tinh.py   # nghiệm thu máy tính dòng tiền
python3 ke-hoach-tang-qua/tang-0/xuat-ban-do.py     # xuất lại bản đồ PNG + PDF
python3 ke-hoach-tang-qua/tang-1/xuat-cam-nang.py   # xuất lại cẩm nang PDF
python3 ke-hoach-tang-qua/tang-1/xuat-12-cau.py     # xuất lại tờ 12 câu hỏi
python3 ke-hoach-tang-qua/tang-2/xuat-bao-cao.py    # xuất báo cáo cá nhân PDF
python3 ke-hoach-tang-qua/phieu-dan/tao-email.py    # sinh lại ba email HTML
```

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
