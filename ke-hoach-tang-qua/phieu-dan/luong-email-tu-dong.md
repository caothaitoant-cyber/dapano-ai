# C2 · Luồng gửi quà tự động

Mục tiêu duy nhất: **khách bấm nút xong, file về hộp thư trong dưới 60 giây.** Chậm hơn là mất người.

> Phụ thuộc: [`landing-page.html`](./landing-page.html) (C1) và webhook trong [`cau-hinh-crm.md`](./cau-hinh-crm.md) (C3).

---

## 1. Ba email và một tin nhắn

| Mốc | Kênh | Mục đích | Không được làm gì |
|---|---|---|---|
| **Ngay lập tức** | Email 1 | Gửi link tải bộ quà | Không chèn lời chào bán |
| **Trong 24 giờ** | Zalo (người thật gọi) | Hỏi file có dùng được không | **Không báo giá, không giới thiệu toà nào** |
| **Sau 48 giờ** | Email 2 | Hướng dẫn dùng Máy Tính Dòng Tiền trong một phút | Không giục |
| **Sau 5 ngày** | Email 3 | Mời làm Báo cáo Sức Khoẻ Dòng Tiền Cá Nhân (Tầng 2) | Không tạo khan hiếm giả |

Sau email 3, nếu khách không phản hồi: chuyển sang tuyến nội dung hằng tuần, **không gửi thêm email mời** cho tới khi khách tự tương tác lại.

## 2. Nội dung email 1 — gửi ngay

**Tiêu đề:** `Bộ Khởi Động Toà Nhà Đầu Tiên của anh/chị đây ạ`

> Dạ em chào anh/chị **{{ho_ten}}**,
>
> Bộ quà của anh/chị đây ạ — em gửi kèm cả ba món:
>
> **1 · Máy Tính Dòng Tiền 10 Năm** *(Excel và Google Sheet)* — [Tải về]({{link_may_tinh}})
> **2 · Cẩm nang "Toà Nhà Đầu Tiên"** *(20 trang, PDF)* — [Tải về]({{link_cam_nang}})
> **3 · Bộ 12 câu hỏi phải hỏi chủ nhà** *(1 trang, in ra cầm theo)* — [Tải về]({{link_12_cau}})
>
> Nếu anh/chị muốn dùng ngay: mở món số 1, chỉ gõ vào những ô màu vàng thôi ạ. Còn lại file tự tính.
>
> Trong một hai ngày tới em xin phép gọi anh/chị một cuộc ngắn — chỉ để hỏi xem file có chỗ nào khó dùng không. Em không chào bán gì trong cuộc gọi đó ạ.
>
> Trân trọng,
> **{{ten_chuyen_vien}}** · DAPANO GROUP
> *Nghĩ Thiện!*

**Bắt buộc:** ba link tải là **link cố định, không hết hạn**. Khách mở lại file sau sáu tháng vẫn phải tải được.

## 3. Nội dung email 2 — sau 48 giờ

**Tiêu đề:** `Một phút để đọc kết quả trong file dòng tiền`

> Dạ anh/chị **{{ho_ten}}**,
>
> Em gửi anh/chị cách đọc nhanh file Máy Tính Dòng Tiền ạ:
>
> **DSCR** là con số quan trọng nhất — dưới 1,2 là đèn đỏ, nghĩa là chỉ cần toà nhà trống hai tháng là anh/chị phải bù tiền túi. Từ 1,5 trở lên thì tiền thuê gánh được nợ.
>
> **Cột "Thận trọng"** ở sheet 3 mới là cột đáng nhìn. Nếu ở cột ấy dòng tiền vẫn dương thì toà nhà chịu được sóng gió. Nếu chỉ cột "Kỳ vọng" mới đẹp, nghĩa là mình đang mua một hy vọng chứ không mua một dòng tiền.
>
> Anh/chị nhập thử một toà đang rao bán vào file rồi nhắn em con số DSCR ra bao nhiêu, em đọc giúp ạ.
>
> **{{ten_chuyen_vien}}** · DAPANO GROUP

## 4. Nội dung email 3 — sau 5 ngày

**Tiêu đề:** `Anh/chị có muốn một bản phân tích riêng cho hồ sơ của mình không ạ?`

> Dạ anh/chị **{{ho_ten}}**,
>
> File dòng tiền tính cho **một toà nhà**. Còn câu hỏi lớn hơn thường là: *với vốn của mình, mình nên nhắm tài sản tầm bao nhiêu và vay được tới đâu?*
>
> Mỗi tháng đội thẩm định bên em nhận một số hồ sơ để làm **Báo cáo Sức Khoẻ Dòng Tiền Cá Nhân**: anh/chị trả lời 12 câu, bên em gửi lại bản phân tích riêng 6 trang — khoảng giá tài sản phù hợp, cấu trúc vốn đề xuất, hai kịch bản dòng tiền và ba rủi ro cần chuẩn bị. Kèm 20 phút gọi giải thích.
>
> Miễn phí ạ. Và trong cuộc gọi đó em **không giới thiệu bất kỳ toà nhà nào** — đó là nguyên tắc của bước này.
>
> [Trả lời 12 câu tại đây]({{link_form_tang_2}})
>
> **{{ten_chuyen_vien}}** · DAPANO GROUP · *Cộng Hưởng Cùng Viên Mãn*

## 5. Tin nhắn Zalo cho sale gọi trong 24 giờ

> "Dạ em chào anh **{{ho_ten}}**, em là **{{ten_chuyen_vien}}** bên DAPANO. Hôm qua anh có tải bộ Máy Tính Dòng Tiền của bên em. Em nhắn không phải để mời gì đâu ạ — em chỉ muốn hỏi anh mở file lên có chỗ nào khó dùng không, để em hướng dẫn anh một phút thôi ạ."

Gọi được thì gọi, không gọi được thì nhắn. **Không gọi quá hai lần** nếu khách không bắt máy.

## 6. Nghiệm thu trước khi bật quảng cáo

- [ ] Tự đăng ký thử **ba lần** bằng ba email khác nhau: Gmail, email công ty, và một hộp thư trên điện thoại.
- [ ] Cả ba lần file về trong **dưới 60 giây**.
- [ ] Không lần nào rơi vào Spam hoặc mục Quảng cáo.
- [ ] Ba link tải đều mở được và **không hết hạn**.
- [ ] Tên khách hiển thị đúng trong email (không còn `{{ho_ten}}`).
- [ ] Huỷ đăng ký hoạt động thật.

## 7. Ba con số phải theo hằng tuần

| Chỉ số | Ngưỡng cần đạt | Nếu không đạt |
|---|---|---|
| Tỷ lệ mở email 1 | trên 60% | Sửa tiêu đề email, kiểm tra vào Spam |
| Tỷ lệ bấm link tải | trên 70% người mở | Link chưa đủ rõ, để lên đầu email |
| Tỷ lệ Tầng 1 → Tầng 2 | trên 10% | **Dừng tăng ngân sách quảng cáo.** Sửa quà và tốc độ gọi trước |

---

**DAPANO GROUP** · Think Kind! · *Cộng Hưởng Cùng Viên Mãn*
