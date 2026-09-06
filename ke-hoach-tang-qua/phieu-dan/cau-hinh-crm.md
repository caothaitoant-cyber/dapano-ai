# C3 · Cấu hình CRM & webhook nhận lead

Lead rơi vào hộp thư cá nhân của một người là lead đã mất. Phần này để mọi lead vào **một chỗ duy nhất**, có người chịu trách nhiệm và có đồng hồ đếm.

---

## 1. Hai luật cứng

| Luật | Con số | Vì sao |
|---|---|---|
| **Nhập CRM** | trong **15 phút** kể từ khi khách gửi form | Tự động hoá làm việc này, không giao cho trí nhớ |
| **Gọi lần đầu** | trong **24 giờ** | Sau 48 giờ khách đã quên mình là ai |

## 2. Trường bắt buộc

| Trường | Nguồn | Ghi chú |
|---|---|---|
| Họ tên | form | |
| SĐT/Zalo | form | Lưu dạng chữ để không mất số 0 đầu |
| Email | form | |
| **Nguồn** | tham số `source` | `landing-tang-1`, `facebook-bai-3`, `ban-do-tang-0`… |
| **Món quà đã tải** | tham số `qua` | Biết khách quan tâm gì trước khi gọi |
| Thành phố nhắm | câu 6 Tầng 2 | Để chia đúng chuyên viên |
| Vốn tự có | câu 1 Tầng 2 | Để sàng lọc |
| Thời điểm xuống tiền | câu 5 Tầng 2 | Để xếp ưu tiên gọi |
| **Tầng đang đứng** | sale cập nhật | 0 · 1 · 2 · 3 · 4 · 5 |
| Lần chạm gần nhất | tự động | Quá 30 ngày không chạm → nhắc |
| Trạng thái | sale cập nhật | Mới · Đang nuôi · Đủ điều kiện · Không phù hợp · Đã giao dịch |

## 3. Chọn công cụ — chốt một, đừng dùng hai

| Phương án | Hợp khi | Điểm yếu |
|---|---|---|
| **Google Sheet + Apps Script** | Bắt đầu ngay trong tuần này, dưới 500 lead | Không có nhắc việc, dễ sửa nhầm |
| **CRM có sẵn** (HubSpot free, Zoho, Getfly, CrmViet…) | Từ 3 sale trở lên, cần phân quyền và nhắc việc | Mất thời gian dựng, có phí |
| **Salekit** (đang dùng để host landing) | Muốn gọn một mối | Cần kiểm xem báo cáo phễu có đủ dùng không |

> **Đề xuất:** chạy Google Sheet trong 30 ngày thử nghiệm để có số thật, rồi mới chọn CRM. Chọn CRM trước khi biết phễu chạy thế nào là chọn mò.

## 4. Webhook Google Apps Script

Dán vào Apps Script gắn với Google Sheet nhận lead, rồi **Deploy → Web app → Who has access: Anyone** *(bắt buộc, nếu không webhook trả lỗi)*. Lấy URL dán vào `DPN_CONFIG.WEBHOOK_URL` trong `landing-page.html`.

```javascript
function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Leads')
               || SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const d = e.parameter || {};
    sheet.appendRow([
      new Date(),                       // thời điểm nhận
      d.fullname || '',                 // họ tên
      "'" + (d.phone || ''),            // dấu ' giữ số 0 đầu
      d.email || '',
      d.source || 'khong-ro',           // nguồn
      d.qua || '',                      // món quà đã tải
      'Mới',                            // trạng thái
      '1'                               // tầng đang đứng
    ]);
    return ContentService.createTextOutput('OK');
  } catch (err) {
    Logger.log('Loi: ' + err);
    return ContentService.createTextOutput('ERROR: ' + err);
  }
}

function doGet() {
  return ContentService.createTextOutput('DAPANO webhook dang chay.');
}
```

**Hàng tiêu đề của sheet `Leads`:**
`Thời điểm · Họ tên · SĐT/Zalo · Email · Nguồn · Quà đã tải · Trạng thái · Tầng · Người phụ trách · Lần chạm gần nhất · Ghi chú`

## 5. Nếu host landing trên salekit.io

Salekit **ghi đè form HTML** — nó tự đổi `action` và bỏ qua `onsubmit`. Vì vậy:

1. Dùng **form widget của salekit**, không dùng form HTML thuần trong `landing-page.html`.
2. Đặt `name` cho ba trường đúng như trong file: `fullname` · `phone` · `email`.
3. Vào panel **"Webhook nhận data"**: URL = URL Apps Script ở trên · Method = **POST** · Enctype = **URL Encoded**.
4. Phần còn lại của `landing-page.html` (hero, nỗi đau, bên trong, hỏi đáp, footer) paste vào các khối **Custom HTML** — CSS đã đặt tiền tố `.dpn-` sẵn để không đụng CSS của salekit.

## 6. Phân lead cho sale

- Lead **Hà Nội** → chuyên viên Hà Nội. Lead **TP.HCM** → chuyên viên TP.HCM. Chưa rõ thành phố → người trực trong ngày.
- Mỗi lead có **đúng một** người phụ trách. Hai người cùng gọi một khách là mất khách.
- Lead không phù hợp (vốn dưới 1,5 tỷ hoặc chưa rõ thời điểm) → gắn thẻ **Đang nuôi**, đưa vào tuyến nội dung, **không đeo bám**. Đây là bước +1 của Hệ thống 8+2.

## 7. Nghiệm thu

- [ ] Gửi một lead thử từ landing page → hàng mới xuất hiện trong sheet dưới 15 giây.
- [ ] Số điện thoại giữ nguyên số 0 đầu.
- [ ] Trường `Nguồn` và `Quà đã tải` hiện đúng.
- [ ] Lead được phân cho đúng người và có nhật ký cuộc gọi đầu tiên.
- [ ] Thử một lead trùng email → không tạo hai hàng gây gọi trùng.

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
