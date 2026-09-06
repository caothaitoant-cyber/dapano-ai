# Bảng chi tiết hạng mục — Thang Quà Dòng Tiền

Phân rã 20 chốt chặn trong [`trang-thai-trien-khai.md`](./trang-thai-trien-khai.md) thành **từng file cụ thể**: làm ở đâu, ruột gồm những gì, ai đưa đầu vào, thế nào là xong.

Quy ước đọc: **Chặn bởi** = chưa xong cái đó thì đừng bắt đầu cái này · **Nghiệm thu** = tiêu chí để nói "xong", không phải cảm tính.

---

## 0. Cấu trúc thư mục đích

```
ke-hoach-tang-qua/
├── README.md                          ✅ kế hoạch tổng
├── thang-qua-dong-tien.html           ✅ bản trình bày
├── trang-thai-trien-khai.md           ✅ bảng chốt chặn
├── bang-chi-tiet-hang-muc.md          ✅ file này
├── 00-du-lieu-goc/
│   ├── cap-rate-hn-hcm.md             ⬜ A1
│   └── ho-so-kiem-chung.md            ⬜ A2
│   └── phan-cong-trach-nhiem.md       ⬜ A3
├── tang-0/
│   └── ban-do-dong-tien.html          ⬜ B1
├── tang-1/
│   ├── cam-nang-toa-nha-dau-tien.md   ⬜ B2
│   ├── may-tinh-dong-tien-spec.md     ⬜ B3-a (đặc tả công thức)
│   ├── may-tinh-dong-tien.xlsx        ⬜ B3-b (file phát cho khách)
│   └── 12-cau-hoi-chu-nha.md          ⬜ B4
├── tang-2/
│   ├── 12-cau-sang-loc.md             ⬜ B5-a
│   └── mau-bao-cao-ca-nhan.html       ⬜ B5-b
├── tang-3/
│   ├── 12-diem-kiem-phap-ly.md        ⬜ B6-a
│   └── hop-dong-thue-mau.md           ⬜ B6-b
├── tang-4/
│   └── ke-hoach-nang-gia-thue-18-thang.md  ⬜ B7
├── phieu-dan/
│   ├── landing-page.html              ⬜ C1
│   ├── luong-email-tu-dong.md         ⬜ C2
│   ├── cau-hinh-crm.md                ⬜ C3
│   └── quy-che-thu-tien-hoan-tien.md  ⬜ C4
├── content/
│   └── 01..08-*.md                    ⬜ C5 (8 file)
└── van-hanh/
    ├── kich-ban-chuyen-tang.md        ⬜ D3
    ├── lich-workshop-fieldtour.md     ⬜ D4
    └── nang-luc-doi-tham-dinh.md      ⬜ D1 + D2
```

---

## Nhóm A — Dữ liệu gốc

### A1 · Bảng Cap Rate & giá thuê thật HN – HCM
**File:** `00-du-lieu-goc/cap-rate-hn-hcm.md` · **Chặn bởi:** không · **Đầu vào:** đội thẩm định

**Ruột:**
- Bảng theo trục phố: *thành phố · tên trục · loại tài sản · diện tích sàn phổ biến · giá chào bán/m² · giá thuê/m²/tháng · Cap Rate quan sát được · số mẫu · thời điểm khảo sát*.
- Tối thiểu **8 trục Hà Nội + 8 trục TP.HCM**, mỗi trục ≥ 3 mẫu thật.
- Ghi rõ nguồn từng dòng: danh mục DAPANO đang vận hành / hồ sơ đã giao dịch / khảo sát thị trường.
- Cột "độ tin cậy": Cao (số của mình) · Trung bình (deal đã xem tận nơi) · Thấp (nghe lại).

**Nghiệm thu:** mỗi con số truy được về một hồ sơ hoặc một lần khảo sát có ngày tháng. Không dòng nào ghi "khoảng chừng".

**Cạm bẫy:** lấy giá chào bán trên chợ mạng làm giá thị trường → Cap Rate ảo, hỏng cả Tầng 0 lẫn Tầng 1.

### A2 · Bộ hồ sơ kiểm chứng công thức
**File:** `00-du-lieu-goc/ho-so-kiem-chung.md` · **Chặn bởi:** không · **Đầu vào:** kế toán + vận hành

**Ruột:** 5 giao dịch đã hoàn tất, mỗi hồ sơ ghi: giá mua thật · chi phí sang tên & môi giới · chi phí cải tạo · giá thuê ký được · tỷ lệ lấp đầy 12 tháng đầu · chi phí vận hành thật/tháng · lãi vay & kỳ hạn · dòng tiền ròng thực nhận từng quý.

**Nghiệm thu:** đủ 5 hồ sơ, mỗi hồ sơ đủ 8 trường trên. Ẩn danh tên khách trước khi đưa vào repo.

**Vì sao gấp:** đây là thước đo duy nhất để biết Máy Tính Dòng Tiền (B3) tính đúng hay tính bậy.

### A3 · Phân công trách nhiệm
**File:** `00-du-lieu-goc/phan-cong-trach-nhiem.md` · **Chặn bởi:** không · **Đầu vào:** anh Toàn quyết

**Ruột:** bảng *tầng · tên món quà · người chịu trách nhiệm · người hỗ trợ · hạn chót · trạng thái*. Thêm dòng "ai được quyền duyệt phát hành ra ngoài" cho từng món.

**Nghiệm thu:** mỗi tầng có đúng **một** cái tên chịu trách nhiệm. Hai tên là không có tên nào.

---

## Nhóm B — Bảy món quà

### B1 · Bản đồ Dòng Tiền HN – TP.HCM (Tầng 0)
**File:** `tang-0/ban-do-dong-tien.html` (xuất PNG A3 + PDF) · **Chặn bởi:** A1

**Ruột:**
- Nửa trái Hà Nội, nửa phải TP.HCM: 8 trục phố mỗi bên, chấm màu theo khoảng Cap Rate.
- Dải chú giải Cap Rate 4 mức màu theo palette DAPANO.
- Hộp "3 dấu hiệu toà nhà ăn được" và "3 dấu hiệu phải tránh".
- Chân trang: nguồn dữ liệu, thời điểm khảo sát, câu dẫn sang Tầng 1 + QR về landing page.

**Nghiệm thu:** in ra A3 đọc được bằng mắt thường; xem trên điện thoại vẫn đọc được tên trục phố; không có ô nào ghi số chưa có nguồn.

**Cạm bẫy:** nhồi 30 trục cho oai → không ai đọc. 8 trục mỗi thành phố là đủ.

### B2 · Cẩm nang "Toà Nhà Đầu Tiên" (Tầng 1)
**File:** `tang-1/cam-nang-toa-nha-dau-tien.md` → dàn trang PDF ~40 trang · **Chặn bởi:** A1, A2

**Ruột — 7 bước:**
1. Xác định mình đang có gì (vốn tự có, khả năng vay, thời gian rảnh).
2. Chọn vùng và loại tài sản hợp với túi tiền — kèm bảng A1.
3. Đọc số một toà nhà: NOI, Cap Rate, DSCR, dòng tiền ròng.
4. Thẩm định pháp lý trước khi đặt cọc.
5. Thu xếp vốn vay: cấu trúc đòn bẩy an toàn, ngưỡng DSCR không được xuống dưới.
6. Cải tạo & định giá lại giá thuê.
7. Vận hành 12 tháng đầu — cái gì tự làm, cái gì thuê.
- Mỗi bước đóng bằng 1 ví dụ số thật (1 HN, 1 HCM, lấy từ A2, đã ẩn danh).
- Phụ lục: bảng thuật ngữ, lời mời tải Máy Tính Dòng Tiền.

**Nghiệm thu:** một người chưa từng mua toà nhà đọc xong tự trả lời được "tôi nên nhắm tầm bao nhiêu tỷ". Mọi ví dụ số đều truy được về A2.

### B3 · Máy Tính Dòng Tiền 10 Năm (Tầng 1) — **trái tim của phễu**
**File:** `tang-1/may-tinh-dong-tien-spec.md` (đặc tả) + `tang-1/may-tinh-dong-tien.xlsx` + bản Google Sheet · **Chặn bởi:** A2

**Ruột — 4 sheet:**
- **Sheet 1 · Nhập liệu** (chỉ ô vàng cho khách gõ): giá mua · chi phí mua (thuế, phí, môi giới) · chi phí cải tạo · vốn tự có · số tiền vay · lãi suất năm 1 · lãi suất thả nổi các năm sau · kỳ hạn vay · giá thuê tháng · số kỳ trống dự kiến/năm · chi phí vận hành/tháng · thuế cho thuê · tỷ lệ tăng giá thuê/năm · tỷ lệ tăng chi phí/năm.
- **Sheet 2 · Kết quả 10 năm:** doanh thu thuê · chi phí vận hành · **NOI** · trả gốc & lãi · **dòng tiền ròng từng năm** · **DSCR** từng năm · dòng tiền luỹ kế · **điểm hoà vốn** (tháng thứ mấy) · **Cap Rate** trên giá mua và trên tổng vốn.
- **Sheet 3 · Ba kịch bản:** thận trọng / cơ sở / kỳ vọng — lệch nhau ở giá thuê, tỷ lệ trống, lãi suất. Bảng so sánh 3 cột.
- **Sheet 4 · Đọc kết quả:** giải thích từng chỉ số bằng tiếng người + ngưỡng cảnh báo (DSCR < 1,2 là đèn đỏ; dòng tiền âm quá 18 tháng là đèn đỏ).

**Nghiệm thu:**
- Chạy lại 5 hồ sơ của A2 → sai lệch dòng tiền ròng năm 1 **dưới 5%** so với số thực nhận.
- Khoá toàn bộ ô công thức, chỉ mở ô nhập.
- Nhập ô rỗng không làm vỡ file (`#DIV/0!` là lỗi nghiệm thu).
- Mở được trên điện thoại bằng Google Sheet.

**Cạm bẫy:** làm quá nhiều nút bấm cho sang. Khách cần **14 ô nhập ra một con số biết nên mua hay không**, không cần mô hình 20 sheet.

### B4 · Bộ 12 câu hỏi phải hỏi chủ nhà (Tầng 1)
**File:** `tang-1/12-cau-hoi-chu-nha.md` → 1 trang PDF · **Chặn bởi:** không (làm được ngay)

**Ruột — 12 chủ đề:** giấy tờ & quy hoạch · tranh chấp/thế chấp · tuổi công trình & kết cấu · điện nước PCCC · hợp đồng thuê đang có (còn bao lâu, giá bao nhiêu) · lịch sử trống · chi phí vận hành thật · phí quản lý & thuế · lý do bán · đã rao bao lâu, đã hạ giá chưa · thời gian bàn giao · những gì để lại trong nhà.
- Mỗi câu kèm **một dòng "nghe câu trả lời này thì phải cảnh giác"**.

**Nghiệm thu:** in vừa 1 trang A4, cầm đi xem nhà tích được.

### B5 · Bộ sàng lọc + mẫu Báo cáo cá nhân (Tầng 2)
**File:** `tang-2/12-cau-sang-loc.md` + `tang-2/mau-bao-cao-ca-nhan.html` · **Chặn bởi:** A1, B3

**Ruột 12 câu sàng lọc:** vốn tự có · nguồn vốn (tiết kiệm/bán tài sản/vay người thân) · khả năng vay & thu nhập chứng minh được · thời điểm dự kiến xuống tiền · thành phố nhắm tới · đã đi xem toà nào chưa · tài sản đang nắm · thu nhập thụ động hiện tại · khẩu vị rủi ro · mục tiêu 5 năm · ai cùng ra quyết định · điều gì đang khiến anh/chị chưa quyết.

**Ruột báo cáo 6–8 trang:** trang 1 tóm tắt 1 trang cho người bận · khoảng giá tài sản phù hợp · cấu trúc vốn đề xuất (vay bao nhiêu %, DSCR dự kiến) · 2 kịch bản dòng tiền từ B3 · 3 rủi ro lớn nhất của riêng hồ sơ này · việc nên làm trong 90 ngày tới · trang cuối: lời mời Tầng 3.

**Nghiệm thu:** làm thử trên **2 khách cũ đã biết kết quả thật** → báo cáo phải nói đúng cái đã xảy ra. Một hồ sơ làm xong trong **dưới 90 phút** (nếu lâu hơn thì 30 hồ sơ/tháng là bất khả thi → xem lại D1).

**Ranh giới:** trong cuộc gọi 20 phút đọc báo cáo **không chào bán toà nào**. Ghi câu này ngay đầu file để sale không quên.

### B6 · Bộ kiểm pháp lý + hợp đồng thuê mẫu (Tầng 3)
**File:** `tang-3/12-diem-kiem-phap-ly.md` + `tang-3/hop-dong-thue-mau.md` · **Chặn bởi:** rà soát pháp lý

**Ruột kiểm pháp lý:** sổ đỏ/hồng & đúng chủ · quy hoạch & lộ giới · giấy phép xây dựng vs hiện trạng · hoàn công · thế chấp · tranh chấp/kê biên · nghĩa vụ thuế · PCCC · giấy phép kinh doanh của khách thuê · hợp đồng thuê đang hiệu lực · quyền ưu tiên thuê tiếp · điều kiện chuyển nhượng.

**Ruột hợp đồng mẫu:** điều khoản chống bỏ cọc, đặt cọc & phạt vi phạm, tăng giá theo chu kỳ, sửa chữa ai chịu, chấm dứt sớm, bàn giao & hoàn trả hiện trạng.

**Nghiệm thu:** **có chữ ký/xác nhận của luật sư hoặc bộ phận pháp lý trước khi phát hành.** Chưa có xác nhận thì không được đưa vào quà Tầng 3.

### B7 · Kế hoạch nâng giá thuê 18 tháng (Tầng 4)
**File:** `tang-4/ke-hoach-nang-gia-thue-18-thang.md` · **Chặn bởi:** A2

**Ruột:** template điền cho từng tài sản — hạng mục cải tạo theo thứ tự hoàn vốn nhanh nhất · chi phí dự kiến từng hạng mục · % tăng giá thuê kỳ vọng · mốc thời gian tháng 1–6–12–18 · mốc định giá lại để tái cấp vốn (nối vào Lớp bán chéo 3 · BRRRR).

**Nghiệm thu:** điền thử cho 1 tài sản đang vận hành, con số cải tạo khớp báo giá thật.

---

## Nhóm C — Đường ống dẫn khách

### C1 · Landing page + form
**File:** `phieu-dan/landing-page.html` · **Chặn bởi:** B2, B3, B4 (phải có quà mới mời tải)

**Ruột:** tiêu đề đánh đúng nỗi đau nhóm A · 3 gạch đầu dòng nói rõ nhận được gì · ảnh bìa bộ quà · **form đúng 3 trường** (tên · SĐT/Zalo · email) · 1 dòng cam kết không spam · phần trả lời 4 câu hỏi ngần ngại thường gặp · không có menu, không có link ra ngoài.

**Nghiệm thu:** tải trên 4G dưới 3 giây · điền form trên điện thoại không phải phóng to · tự đăng ký thử 3 lần đều nhận được file.

### C2 · Luồng gửi file tự động
**File:** `phieu-dan/luong-email-tu-dong.md` · **Chặn bởi:** C1

**Ruột:** email 1 gửi ngay (link tải bộ quà, dưới 60 giây) · email 2 sau 48 giờ (hướng dẫn dùng Máy Tính Dòng Tiền, 1 phút) · email 3 sau 5 ngày (mời Tầng 2) · tin nhắn Zalo mẫu cho sale gọi trong 24 giờ · quy định link tải không hết hạn.

**Nghiệm thu:** bấm gửi → file về hộp thư trong **dưới 1 phút**, thử cả Gmail và mail công ty, không rơi vào Spam.

### C3 · Cấu hình CRM
**File:** `phieu-dan/cau-hinh-crm.md` · **Chặn bởi:** A3 (ai quản CRM), C1

**Ruột:** chốt dùng CRM nào · các trường bắt buộc (nguồn · món quà đã tải · thành phố nhắm · vốn tự có · tầng đang đứng · lần chạm gần nhất) · webhook từ form về CRM · quy định **nhập trong 15 phút** và **gọi trong 24 giờ** · cách gắn thẻ khách không phù hợp để chuyển sang danh sách nuôi dưỡng (bước +1).

**Nghiệm thu:** một lead thử chạy trọn đường form → CRM → phân cho sale → có nhật ký cuộc gọi.

### C4 · Quy chế thu tiền & hoàn tiền Tầng 3
**File:** `phieu-dan/quy-che-thu-tien-hoan-tien.md` · **Chặn bởi:** A3

**Ruột:** kênh thu 299.000đ và 1.000.000đ · xuất hoá đơn thế nào · **văn bản cam kết hoàn 100% vào giá trị giao dịch trong 90 ngày** (điều kiện, ai duyệt, hạch toán vào đâu) · chính sách khách đăng ký rồi không đi.

**Nghiệm thu:** kế toán xác nhận hạch toán được; câu chữ cam kết hoàn tiền đã qua pháp lý.

### C5 · Tám bài content
**File:** `content/01..08-*.md` · **Chặn bởi:** B1, B2, B3 (bài dẫn về đâu thì thứ đó phải có thật)

| # | Bài | Công thức | Dẫn về | Điều kiện riêng |
|---|---|---|---|---|
| 1 | 12 trục phố cho thuê tốt nhất HN & HCM | List/Tips | Tầng 0 | Cần A1 |
| 2 | Gửi tiết kiệm 5 tỷ, mỗi tháng mất bao nhiêu vì trượt giá | PAS | Tầng 1 | — |
| 3 | Không phải cứ mặt phố là ra tiền — ba toà đã khuyên khách bỏ | Myth Busting | Tầng 1 | Số từ hồ sơ thật |
| 4 | Anh đang ở đâu trên đường tới toà nhà đầu tiên | Question/Engage | Tầng 2 | — |
| 5 | Anh T., chủ xưởng gỗ: từ 4 tỷ nằm im tới 62 triệu/tháng | Before-After-Bridge | Tầng 2 | **Bắt buộc có testimonial thật + giấy xin phép khách** |
| 6 | Nghề của em không phải bán nhà. Nghề của em là đọc số | Enemy/Reframe | Tầng 3 | — |
| 7 | Buổi sáng em đi xem toà nhà thứ 47 trong năm nay | Story | Tầng 3 | — |
| 8 | Buổi khảo sát thực địa tháng này còn 3 chỗ | Direct Response | Tầng 3 | Chỉ đăng khi **thật sự** còn 3 chỗ |

**Nghiệm thu từng bài:** đúng công thức đã gán · đúng 1 nỗi đau · đúng 1 lời mời · không có câu nào vi phạm mục 10 (ranh giới) của kế hoạch.

### C6 · Ngân sách & người chạy quảng cáo
**Ghi vào:** `00-du-lieu-goc/phan-cong-trach-nhiem.md` · **Chặn bởi:** C1, C2, C5

**Ruột:** ngân sách thử tháng đầu cho mỗi thành phố · ai cầm tài khoản quảng cáo · ngưỡng chi phí mỗi lead Tầng 1 chấp nhận được · quy định **không tăng ngân sách khi tỷ lệ Tầng 1→2 dưới 10%**.

---

## Nhóm D — Vận hành & năng lực thật

### D1 + D2 · Năng lực đội thẩm định và danh mục
**File:** `van-hanh/nang-luc-doi-tham-dinh.md`

**Ruột:** số giờ thật để làm 1 Báo cáo cá nhân × 30 hồ sơ = có kham nổi không · danh sách toà sẵn sàng cho field tour (cần **≥ 6**, ghi rõ toà nào ở đâu, chủ có đồng ý cho xem không) · số chuyên viên đi tour được.

**Nghiệm thu:** một con số thật thay cho con số 30. Nếu chỉ kham 15 thì **sửa kế hoạch xuống 15** — kế hoạch cấm khan hiếm giả.

### D3 · Diễn thử kịch bản chuyển tầng
**File:** `van-hanh/kich-ban-chuyen-tang.md` · **Chặn bởi:** B3, B5

**Ruột:** 3 kịch bản đã có trong README + phần bổ sung: câu trả lời cho 6 phản đối hay gặp · checklist sale tự chấm sau mỗi cuộc gọi · quy định ghi lại quê quán/nghề/tên con vào CRM (Bước 3).

**Nghiệm thu:** mỗi sale diễn thử trọn 1 lượt, có người đóng vai khách khó; ai chưa qua thì chưa được nhận lead.

### D4 · Lịch workshop & field tour
**File:** `van-hanh/lich-workshop-fieldtour.md` · **Chặn bởi:** D1, D2, C4

**Ruột:** ngày cụ thể 3 tháng tới — 2 workshop/tháng, 1 field tour/tháng mỗi thành phố, tối đa 8 người/tour · ai dẫn · toà nào đi xem · kịch bản 3 giờ workshop.

**Nghiệm thu:** lịch có ngày giờ thật, đã đặt vào lịch của người dẫn.

---

## Thứ tự triển khai đề xuất

| Tuần | Làm gì | Vì sao thứ tự này |
|---|---|---|
| **1** | A1 · A2 · A3 · B4 | Không có số thì mọi thứ sau là văn bản đẹp. B4 làm song song vì không phụ thuộc gì |
| **2** | B3 (spec → file → kiểm chứng bằng A2) · B1 | Trái tim của phễu, và món dễ lan truyền nhất |
| **3** | B2 · B5 · C5 bài 1–4 | Có ruột số rồi mới viết được cẩm nang và báo cáo |
| **4** | C1 · C2 · C3 · D3 | Dựng ống dẫn và luyện sale, xong là bật quảng cáo nhỏ |
| **5+** | B6 · B7 · C4 · D1 · D2 · D4 · C5 bài 5–8 | Tầng 3 trở lên, chạy sau khi Tầng 0–2 đã có số đo |

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
