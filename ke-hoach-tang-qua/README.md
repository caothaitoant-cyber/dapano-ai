# Thang Quà Dòng Tiền

Kế hoạch tặng quà (lead magnet + phễu bán chéo nhiều tầng) cho DAPANO GROUP — thu hút và nuôi dưỡng nhà đầu tư quan tâm tới toà nhà dòng tiền tại **Hà Nội** và **TP.HCM**.

Bản trình bày đầy đủ: [`thang-qua-dong-tien.html`](./thang-qua-dong-tien.html) (chuẩn nhận diện DAPANO, in/chia sẻ được).

**Bắt đầu chạy: [`KHOI-DONG.md`](./KHOI-DONG.md) — runbook 7 ngày.**

Tiến độ triển khai & bốn thứ đang chặn phễu: [`trang-thai-trien-khai.md`](./trang-thai-trien-khai.md).
Bảng phân rã từng file: [`bang-chi-tiet-hang-muc.md`](./bang-chi-tiet-hang-muc.md).

## Quà và công cụ đã dựng xong

| Tầng | File dùng được ngay |
|---|---|
| **Tầng 0** | [`tang-0/ban-do-dong-tien.html`](./tang-0) — bản đồ A3 (+ PNG, PDF), chờ số Cap Rate thật |
| **Tầng 1** | [`tang-1/may-tinh-dong-tien.xlsx`](./tang-1) · [`cẩm nang 20 trang`](./tang-1/cam-nang-toa-nha-dau-tien.pdf) · [`12 câu hỏi chủ nhà`](./tang-1/12-cau-hoi-chu-nha.md) |
| **Tầng 2** | [`tang-2/12-cau-sang-loc.md`](./tang-2) · mẫu báo cáo 6 trang tự tính số |
| **Tầng 3** | [`tang-3/`](./tang-3) — bộ 12 điểm kiểm pháp lý và hợp đồng thuê mẫu *(bản thảo, chờ pháp lý duyệt)* |
| **Tầng 4** | [`tang-4/ke-hoach-nang-gia-thue-18-thang.md`](./tang-4) |
| **Phễu** | [`phieu-dan/`](./phieu-dan) — landing page, form Tầng 2, trang Tầng 3, ba email HTML, CRM, quy chế thu tiền |
| **Content** | [`content/`](./content) — 8 bài theo 8 công thức |
| **Vận hành** | [`van-hanh/`](./van-hanh) — kịch bản sale, năng lực đội, lịch workshop & field tour |

Xuất lại PDF/PNG: `python3 tang-0/xuat-ban-do.py` · `tang-1/xuat-cam-nang.py` · `tang-2/xuat-bao-cao.py`
Nghiệm thu máy tính dòng tiền: `python3 tang-1/kiem-chung-may-tinh.py`
Điền link và số vào mọi trang: điền [`cau-hinh.json`](./cau-hinh.json) rồi chạy `python3 ap-cau-hinh.py`

---

## 1. Nguyên tắc thiết kế quà

Một toà nhà dòng tiền là quyết định 8–50 tỷ. Không ai ký vì một mẩu quảng cáo hay. Quà là **cây cầu** bắc qua từng đoạn của hành trình *hiểu — tin — tự kiểm chứng — nhìn tận mắt — xuống tiền*.

Ba nguyên tắc bắt buộc cho mọi món quà:

1. **Dùng được ngay** — mở ra là tính được ngay dòng tiền căn đang nhắm.
2. **Tự phơi bày nhu cầu** — khách nhập số vốn, giá thuê, thời điểm mua là đã tự làm Bước 4 (Xác định nhu cầu) thay cho sale.
3. **Dẫn tới tầng sau** — mỗi món kết thúc bằng một lời mời cụ thể lên tầng kế tiếp.

Tặng quà chính là **Bước 2 trong Hệ thống Bán hàng 8+2** — tạo lý do chính đáng để ngồi lâu hơn với anh/chị nhà đầu tư. Cho đi từ chữ **Nhân**, giữ đúng hẹn bằng chữ **Tín**.

## 2. Ba nhóm người nhận quà

| Nhóm | Chân dung | Nỗi đau nói thành lời | Quà chạm đúng |
|---|---|---|---|
| **A · Người tích luỹ** | 40–55 tuổi, 1,5–5 tỷ nhàn rỗi, đang gửi tiết kiệm / ôm đất nền | "Tiền để ngân hàng thì lãi không đủ trượt giá, mà mua đất thì nằm im mấy năm nay rồi." | Tầng 1 · Máy tính dòng tiền |
| **B · Chủ doanh nghiệp** | 38–52 tuổi, vốn 5–20 tỷ, vay được ngân hàng | "Nếu ngày mai công ty khó thì nhà tôi sống bằng gì?" | Tầng 2 · Báo cáo sức khoẻ dòng tiền |
| **C · NĐT có kinh nghiệm** | 35–55 tuổi, đã có 1–3 BĐS cho thuê, muốn lên toà nhà | "Lên toà nhà thì pháp lý và vận hành tôi chưa nắm." | Tầng 3 · Khảo sát thực địa |

> Nhóm A cần được trấn an. Nhóm B cần được che chắn. Nhóm C cần được nhìn tận mắt.

## 3. Thang quà 6 tầng

Xếp theo **mức cam kết khách phải bỏ ra**: không mất gì → để lại số điện thoại → nói thật về tài chính → trả tiền → ký hợp đồng. Không được nhảy cóc — nhảy cóc chính là lỗi báo giá sớm mà 8+2 cấm.

### Tầng 0 — Quà mở cửa (miễn phí, không cần để lại thông tin)
**Bản đồ Dòng Tiền Hà Nội – TP.HCM** — 1 trang A3 (ảnh + PDF):
- Các trục phố cho thuê đang có nhu cầu thật ở hai thành phố + khoảng Cap Rate tham chiếu do đội thẩm định DAPANO khảo sát.
- 3 dấu hiệu nhận biết toà nhà "ăn được" và 3 dấu hiệu phải tránh.

*Mục tiêu:* reach & lưu về máy, **không thu lead**. *Lối ra:* "Muốn tính thử toà nhà anh/chị đang nhắm? Nhận file tính dòng tiền ở Tầng 1."

### Tầng 1 — Quà đổi danh tính (miễn phí, đổi lấy tên · SĐT/Zalo · email)
**Bộ Khởi Động Toà Nhà Đầu Tiên**:
1. **Cẩm nang "Toà Nhà Đầu Tiên"** — 7 bước sở hữu một tài sản tự trả nợ cho mình (~40 trang, ví dụ số thật ở cả HN và HCM).
2. **Máy Tính Dòng Tiền 10 Năm** (Excel/Google Sheet) — nhập giá mua, giá thuê, lãi vay, chi phí vận hành → ra NOI, Cap Rate, DSCR, dòng tiền ròng từng năm, điểm hoà vốn.
3. **Bộ 12 câu hỏi phải hỏi chủ nhà** trước khi đặt cọc.

*Vì sao món 2 là trái tim:* khách mở lại nhiều lần — mỗi lần mở là một lần nhớ DAPANO, mỗi con số nhập vào là một mẩu dữ liệu về ngân sách thật.

### Tầng 2 — Quà đổi sự thật (miễn phí, giới hạn 30 hồ sơ/tháng)
**Báo cáo Sức Khoẻ Dòng Tiền Cá Nhân**:
- Khách trả lời 12 câu: vốn tự có, khả năng vay, thời điểm xuống tiền, khẩu vị rủi ro, mục tiêu 5 năm, tài sản đang nắm.
- DAPANO trả lại PDF 6–8 trang **riêng cho khách**: khoảng giá tài sản phù hợp, cấu trúc vốn đề xuất, 2 kịch bản dòng tiền (thận trọng & kỳ vọng), rủi ro cần chuẩn bị.
- Kèm 20 phút gọi giải thích — **không chào bán bất kỳ toà nhà nào** trong cuộc gọi này.

*Đây chính là bước +1 (Xác thực & kiểm tra).* Giới hạn 30 hồ sơ là **năng lực thật** của đội thẩm định, không phải con số bịa tạo sức ép.

### Tầng 3 — Quà có giá (tripwire, hoàn 100% vào giao dịch)
- **A. Workshop online 3 giờ · 299.000đ** — "Giải mã toà nhà dòng tiền HN – HCM". Tặng kèm *Bộ 12 điểm kiểm pháp lý toà nhà* + *Hợp đồng thuê mẫu chống rủi ro bỏ cọc*. Nhịp: 2 buổi/tháng.
- **B. Vé khảo sát thực địa · 1.000.000đ** — 1 buổi xem 3 toà nhà thật cùng chuyên viên thẩm định, đọc số tại chỗ. Hoàn 100% vào giá trị giao dịch nếu mua trong 90 ngày. Nhịp: 1 buổi/tháng mỗi thành phố, tối đa 8 người.

*Mục tiêu không phải tiền* — mà là biến "người xem" thành "người đã trả tiền cho DAPANO một lần", rào cản tâm lý lớn nhất trên đường tới quyết định 10 tỷ.

### Tầng 4 — Sản phẩm lõi (8–50 tỷ)
Quà đi kèm khi ký hợp đồng:
- **12 tháng vận hành cho thuê miễn phí** — tìm khách, ký hợp đồng, thu tiền, xử lý sự cố.
- **Chứng thư thẩm định giá độc lập** + hồ sơ pháp lý đầy đủ bàn giao cùng tài sản.
- **Kế hoạch nâng giá thuê 18 tháng** — cải tạo hạng mục nào trước, chi bao nhiêu, kỳ vọng tăng bao nhiêu %.

Gói "12 tháng vận hành" chính là **cửa vào của toàn bộ tầng bán chéo dịch vụ**.

### Tầng 5 — Quà giữ khách: Câu lạc bộ Chủ Toà Nhà
- Sinh hoạt mỗi quý tại HN và HCM.
- **Quyền xem deal trước thị trường 48 giờ** — đặc quyền đắt giá nhất, không tốn thêm chi phí để trao.
- **Báo cáo thị trường thuê HN – HCM hằng quý**, dữ liệu từ chính danh mục DAPANO đang vận hành.

Khách Tầng 4 mua một lần. Khách Tầng 5 mua toà thứ hai, thứ ba — và giới thiệu người khác (bước +2).

## 4. Năm lớp bán chéo

| Lớp | Bán chéo cái gì | Thời điểm mở lời | Vì sao khách gật |
|---|---|---|---|
| **1 · Vùng** | Chủ toà HN mua thêm toà HCM và ngược lại | Sau 12–18 tháng, khi toà đầu chạy ổn | Hai thị trường lệch pha — nắm cả hai là phân tán rủi ro vùng |
| **2 · Dịch vụ quanh tài sản** | Thẩm định giá · pháp lý & sang tên · thiết kế cải tạo · môi giới cho thuê · quản lý vận hành từ năm 2 · thu xếp vốn vay · bảo hiểm | Ngay trong và sau giao dịch | Đã tin giao 10 tỷ thì không đi tìm bên thứ hai cho việc nhỏ hơn |
| **3 · Chu kỳ (BRRRR)** | Nâng giá thuê → định giá lại → tái cấp vốn → mua toà thứ hai | Tháng 12–18 sau giao dịch | Không phải bỏ thêm tiền túi — **lớp có giá trị vòng đời cao nhất** |
| **4 · Tri thức** | Khoá đào tạo · coaching danh mục 1-1 · tư vấn chuyển giao tài sản | Khi khách có từ 2 tài sản | Người có tài sản lo giữ và trao lại, mạnh hơn cả lo kiếm thêm |
| **5 · Mạng lưới** | Mỗi chủ toà giới thiệu 2 người cùng khẩu vị | Sau kỳ vận hành đầu có kết quả | Thưởng bằng miễn phí vận hành thêm quý, không bằng tiền mặt — giữ chữ **Nghĩa** |

> **Nguyên tắc:** chỉ mở lời bán chéo khi lớp trước đã cho khách một kết quả nhìn thấy được. Bán chéo trên niềm tin đi vay thì phải trả lãi rất đắt.

## 5. Quà nào phục vụ bước nào trong 8+2

| Bước | Tên bước | Quà đảm nhiệm | Việc sale phải làm |
|---|---|---|---|
| 1 | Thu thập thông tin | Form Tầng 1 | Nhập CRM trong 15 phút, ghi rõ nguồn và món quà đã tải |
| 2 | Tạo lý do hẹn gặp | Tầng 0 & 1 | Gọi trong 24 giờ, lý do là *hỏi file có dùng được không* — không chào bán |
| 3 | Xây quan hệ thân tình | Cuộc gọi 20 phút Tầng 2 | Ghi lại quê quán, nghề nghiệp, tên con — và nhớ đúng ở lần sau |
| 4 | Xác định nhu cầu | 12 câu hỏi Tầng 2 | Hỏi sâu vào ô khách để trống — chỗ trống thường là chỗ đau |
| 5 | Trình bày giải pháp | PDF Báo cáo cá nhân + field tour | Chỉ trình bày 1–2 toà khớp đúng báo cáo, không trải hết danh mục |
| 6 | Chốt đơn | Gói quà ký hợp đồng Tầng 4 | Báo giá đầy đủ, không phí ẩn |
| 7 | Xử lý từ chối | Down-sell về Tầng 3 | Chưa đủ vốn → mời workshop, giữ trong CLB, hẹn lại sau 6 tháng |
| 8 | Chăm sóc | Vận hành 12 tháng + CLB | Báo cáo đúng hạn hằng tháng, kể cả tháng có tin xấu |
| +1 | Xác thực & kiểm tra | Toàn bộ Tầng 2 | Khách không phù hợp → chuyển danh sách nuôi dưỡng, không đeo bám |
| +2 | Xin giới thiệu | Sinh hoạt CLB Tầng 5 | Chỉ xin sau khi đã phục vụ có kết quả |

## 6. Ba kịch bản chuyển tầng

**Tầng 1 → Tầng 2 (gọi Zalo sau 48 giờ):**
> "Dạ em chào anh Minh, em là Linh bên DAPANO. Hôm kia anh có tải file Máy tính dòng tiền của bên em. Em gọi không phải để mời gì đâu ạ — em chỉ muốn hỏi anh mở file lên có chỗ nào khó dùng không, để em hướng dẫn anh một phút thôi."
>
> *(nghe khách kể → tìm điểm chung → "Anh đang nhắm khu nào ạ?")*
>
> "Nếu anh muốn, tháng này bên em còn nhận thêm mấy hồ sơ làm Báo cáo sức khoẻ dòng tiền cá nhân. Anh trả lời 12 câu, bên em làm cho anh một bản riêng — anh xem xong biết ngay mình nên nhắm tài sản tầm bao nhiêu và vay được đến đâu. Miễn phí ạ."

**Tầng 2 → Tầng 3 (cuối cuộc gọi đọc báo cáo):**
> "Vậy là theo báo cáo, khoảng phù hợp với anh là 12–16 tỷ, vay 45%, dòng tiền ròng dương từ khoảng tháng thứ tư. Anh thấy con số này có sát với dự tính của anh không ạ?"
>
> *(chờ khách xác nhận — không chuyển tiếp nếu khách còn lăn tăn về số)*
>
> "Số trên giấy thì đẹp, nhưng em nghĩ anh nên nhìn tận mắt một lần. Cuối tháng bên em có buổi đi xem 3 toà thật ở Hà Nội, tám người thôi. Vé một triệu, và nếu anh mua trong 90 ngày thì bên em hoàn hết vào giá trị giao dịch. Em giữ chỗ cho anh nhé?"

**Tầng 4 → Tầng 5 (báo cáo vận hành tháng thứ 10):**
> "Dạ anh Minh, mười tháng vừa rồi toà nhà lấp đầy 92%, giá thuê đã nhích lên được hai đợt. Em gửi anh báo cáo tổng kết năm đầu ạ."
>
> *(chỉ nói tiếp khi con số thật sự tốt — nếu chưa tốt, nói thẳng lý do và kế hoạch xử lý)*
>
> "Với đà này, khoảng tháng 15–18 anh có thể định giá lại và tái cấp vốn, lấy phần vốn dôi ra để nhìn sang một toà trong TP.HCM. Em mời anh vào Câu lạc bộ Chủ Toà Nhà ạ."

## 7. Content kéo người vào thang quà (4 tuần xoay vòng)

| Tuần | Bài | Công thức | Nỗi đau chính | Dẫn về |
|---|---|---|---|---|
| 1 | "12 trục phố cho thuê tốt nhất HN & HCM" | #6 List/Tips | Không biết bắt đầu từ đâu | Tầng 0 |
| 1 | "Gửi tiết kiệm 5 tỷ, mỗi tháng anh mất bao nhiêu vì trượt giá?" | #1 PAS | Tiền đứng yên, sợ già nghèo | Tầng 1 |
| 2 | "Không phải cứ mặt phố là ra tiền — ba toà em đã khuyên khách bỏ" | #5 Myth Busting | Tin vị trí thay vì tin số | Tầng 1 |
| 2 | "Anh đang ở đâu trên đường tới toà nhà đầu tiên?" | #7 Question/Engage | Chưa tự định vị được mình | Tầng 2 |
| 3 | "Anh T., chủ xưởng gỗ: từ 4 tỷ nằm im tới 62 triệu/tháng" | #4 Before-After-Bridge | Sợ đầu tư ngoài ngành mình hiểu | Tầng 2 |
| 3 | "Nghề của em không phải bán nhà. Nghề của em là đọc số." | #8 Enemy/Reframe | Ngán môi giới chỉ chăm chăm chốt | Tầng 3 |
| 4 | "Buổi sáng em đi xem toà nhà thứ 47 trong năm nay" | #2 Story | Không có ai đi cùng khi ra quyết định lớn | Tầng 3 |
| 4 | "Buổi khảo sát thực địa tháng này còn 3 chỗ" | #3 Direct Response | Trì hoãn hết tháng này qua tháng khác | Tầng 3 |

Bài #4 chỉ được đăng khi đã có testimonial thật và đã xin phép khách. Mọi con số phải lấy từ hồ sơ có thật.

## 8. Lộ trình 90 ngày

**Ngày 1–30 · Dựng quà** — T1: chốt nội dung Tầng 0 & 1, khảo sát Cap Rate thật · T2: hoàn thiện Máy tính dòng tiền, kiểm tra công thức bằng 5 hồ sơ đã giao dịch · T3: landing page + form + webhook về CRM · T4: dựng 12 câu hỏi và mẫu Báo cáo cá nhân, đào tạo sale 3 kịch bản.

**Ngày 31–60 · Chạy thử & đo** — T5: mở quảng cáo ngân sách nhỏ ở cả hai thành phố, đăng đủ 8 bài · T6: làm 30 Báo cáo cá nhân đầu tiên · T7: workshop online số 1, đo tỷ lệ Tầng 2→3 · T8: field tour số 1 tại Hà Nội, thay số giả định bằng số thật.

**Ngày 61–90 · Nhân rộng & mở bán chéo** — T9: dồn ngân sách vào kênh có chi phí lead thấp nhất · T10: field tour TP.HCM, bắt đầu deal ưu tiên 48 giờ · T11: mở gói dịch vụ Lớp 2 cho khách hiện hữu, chuẩn bị sinh hoạt CLB · T12: tổng kết phễu, viết lại kế hoạch quý sau.

## 9. Phễu mục tiêu 90 ngày

> Đây là **chỉ tiêu giả định để dựng ngân sách**, chưa phải số thật. Sau 30 ngày chạy thử, thay bằng số đo được và tính lại toàn bộ.

| Chặng | Số lượng | Tỷ lệ chuyển | Điều kiện để đạt |
|---|---:|---:|---|
| Tiếp cận (organic + ads) | 300.000 | — | 8 bài/tháng + ngân sách quảng cáo ổn định |
| Vào landing page | 9.000 | 3% | Tiêu đề đúng nỗi đau, ảnh bìa rõ ràng |
| Để lại thông tin (Tầng 1) | 2.700 | 30% | Form 3 trường, gửi file tự động trong 1 phút |
| Đủ điều kiện sau sàng lọc | 400 | 15% | Vốn tự có từ 1,5 tỷ, có ý định trong 12 tháng |
| Nhận Báo cáo cá nhân (Tầng 2) | 90 | 22% | Năng lực 30 hồ sơ/tháng của đội thẩm định |
| Trả tiền vào Tầng 3 | 45 | 50% | Kịch bản chuyển tầng được dùng đúng |
| Đi xem toà nhà thật | 18 | 40% | Có ít nhất 6 toà trong danh mục sẵn sàng |
| **Giao dịch** | **3 – 5** | 20% | Hồ sơ pháp lý sạch, thu xếp được vốn vay |

**Ba chỉ số theo hằng tuần:** chi phí mỗi lead Tầng 1 · tỷ lệ Tầng 1→2 · tỷ lệ Tầng 2→3.

**Dấu hiệu phải dừng lại xem xét:** Tầng 1→2 dưới 10% nghĩa là quà Tầng 1 hấp dẫn sai người, hoặc sale gọi quá muộn. Sửa quà và tốc độ gọi **trước khi** tăng ngân sách quảng cáo.

## 10. Ranh giới không được bước qua

- ❌ Hứa "làm giàu nhanh", "x2 tài sản trong 6 tháng", lướt sóng.
- ❌ Cam kết lợi nhuận cố định kiểu trái phiếu. Cap Rate là kỳ vọng có cơ sở, không phải lời hứa.
- ❌ Chào condotel, BĐS nghỉ dưỡng, đất nền đầu cơ dưới danh nghĩa dòng tiền.
- ❌ Nhận khách vốn dưới 500 triệu vào phễu bán — mời họ ở lại tuyến nội dung miễn phí.
- ❌ Khan hiếm giả. Giới hạn 30 hồ sơ và 8 chỗ field tour là giới hạn năng lực **thật**.
- ❌ Mượn ngôn ngữ của các vụ việc đã gây mất niềm tin trên thị trường, kể cả để châm biếm.

> Món quà tốt nhất DAPANO có thể tặng một nhà đầu tư, đôi khi là câu *"thời điểm này anh chưa nên mua"*.

## 11. Việc của tuần đầu tiên

1. **Ngày 1** — Chốt tên chính thức Tầng 1 và người chịu trách nhiệm từng tầng.
2. **Ngày 2** — Rút số Cap Rate và giá thuê thật từ danh mục đang vận hành làm ruột cho Tầng 0.
3. **Ngày 3** — Dựng khung Máy tính dòng tiền, kiểm chứng bằng 3 hồ sơ đã giao dịch xong.
4. **Ngày 4** — Viết 12 câu hỏi Tầng 2, thử hỏi trực tiếp 2 khách cũ.
5. **Ngày 5** — Dựng landing page và luồng gửi file tự động, tự đăng ký thử 3 lần.
6. **Ngày 6** — Đào tạo sale 3 kịch bản chuyển tầng, mỗi người diễn thử một lượt.
7. **Ngày 7** — Đăng bài đầu tiên (#6 List/Tips), mở quảng cáo thử, bắt đầu đếm.

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
