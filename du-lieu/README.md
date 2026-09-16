# KHO DỮ LIỆU CHUNG

Bảy bảng CSV dưới đây là **nguồn sự thật duy nhất** về khách hàng, tài sản, tiền và công việc
của DAPANO. Cả 9 phòng ban đọc và ghi vào đúng bảy file này.

> **Không sửa tay file CSV.** Luôn ghi qua công cụ:
> ```bash
> python3 cong-cu/dpn.py them khach-hang ho_ten="Chị Lan" sdt=09xxxxxxxx nhom=A
> ```
> Công cụ tự sinh mã, tự điền ngày, chặn sai cột, và ghi nhật ký vào `nhat-ky-ghi.log`.

## Bốn lệnh cần nhớ

| Lệnh | Việc |
|---|---|
| `python3 cong-cu/dpn.py bang` | Xem 7 bảng, cột nào bắt buộc |
| `python3 cong-cu/dpn.py them <bảng> cột=giá_trị ...` | Thêm một dòng mới |
| `python3 cong-cu/dpn.py sua <bảng> <mã> cột=giá_trị` | Sửa một dòng đã có |
| `python3 cong-cu/dpn.py xem <bảng> --loc nhom=A --so 10` | Tra cứu |
| `python3 cong-cu/dpn.py tong-quan` | Bảng điều khiển nhanh toàn công ty |

## Bảy bảng

### `khach-hang.csv` — mã `KH-xxxx`
Mỗi nhà đầu tư một dòng, không bao giờ trùng.

| Cột | Ý nghĩa | Giá trị nên dùng |
|---|---|---|
| `nhom` | Nhóm chân dung | `A` tích luỹ · `B` chủ doanh nghiệp · `C` có kinh nghiệm |
| `nguon` | Khách đến từ đâu | tên chiến dịch, `gioi-thieu`, `BNI`, `su-kien` |
| `tang_qua` | Đang ở tầng quà nào | `0`–`5` |
| `buoc_8_2` | Đang ở bước nào của hệ thống 8+2 | `1`–`8`, `+1`, `+2` |
| `ngan_sach` | Vốn khách nói ra | ghi đúng lời khách, không suy diễn |
| `phu_trach` | Ai đang cầm khách | tên người thật |
| `trang_thai` | | `moi` · `dang-nuoi` · `nong` · `da-ky` · `nguoi` · `tu-choi` |

### `tuong-tac.csv` — mã `TT-xxxx`
Mỗi lần chạm khách một dòng: gọi, nhắn, gặp, gửi quà. **Đây là trí nhớ về lời đã hứa.**
Cột `hen_tiep_theo` là thứ phòng Điều phối dùng để nhắc việc mỗi sáng.

### `toa-nha.csv` — mã `TN-xxxx`
Kho tài sản đã khảo sát/thẩm định. `noi_nam_1`, `cap_rate`, `dscr`, `tran_gia_mua` chỉ được
điền bởi phòng Thẩm định sau khi chạy đủ 8 bước định giá — không ai khác được điền.

### `giao-dich.csv` — mã `GD-xxxx`
`loai`: `moi-gioi` · `tham-dinh` · `workshop` · `khao-sat` · `van-hanh` · `mentoring`.
`ngay_ky` trống = chưa ký. `ngay_thu` trống mà đã ký = **công nợ phải thu**.

### `chien-dich.csv` — mã `CD-xxxx`
Một chiến dịch marketing một dòng. `chi_phi` ÷ `lead_thu_duoc` = chi phí/lead — chỉ số sống còn
của phòng Marketing.

### `cong-viec.csv` — mã `CV-xxxx`
Hàng đợi việc của cả công ty. `phong_ban`: `P0`–`P8`. `trang_thai`: `moi` · `dang-lam` ·
`cho-duyet` · `xong` · `huy`. Việc quá `han` mà chưa `xong` sẽ hiện đỏ ở `tong-quan`.

### `thu-chi.csv` — mã `TC-xxxx`
`loai`: `thu` hoặc `chi`. Mọi khoản chi phải có `phong_ban` chịu trách nhiệm.

## Quy tắc dữ liệu

1. **Không xoá dòng.** Sai thì đổi `trang_thai` thành `huy` và ghi lý do vào `ghi_chu`.
2. **Số tiền ghi bằng đồng**, viết `1.200.000.000` hoặc `1200000000` đều được.
3. **Ngày ghi dạng `YYYY-MM-DD`.**
4. **Mọi dòng liên quan tới khách phải có `ma_kh`** — không có mã thì tạo khách trước.
5. Cuối mỗi phiên làm việc, commit lại `du-lieu/` để giữ lịch sử thay đổi.
