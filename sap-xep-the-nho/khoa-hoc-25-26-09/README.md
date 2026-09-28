# Khoá học 25–26/09/2026: sắp xếp video lên Google Drive

100 file quay bằng máy DJI (`DJI_20260925091116_0135_D` → `DJI_20260926193123_0234_D`), xếp theo **Ngày → Vòng → Người chia sẻ**. Tên file DJI đã chứa sẵn ngày giờ bắt đầu quay (`DJI_NămThángNgàyGiờPhútGiây_Số_D`), nên thời gian được đọc thẳng từ tên file.

## Cấu trúc trên Google Drive

```
KhoaHoc_25-26_09_2026\
├── Ngay_1_25-09-2026\
│   ├── Vong_1_Sang_09h11-12h51\
│   │   ├── 1_Thay_giao_chia_se\
│   │   ├── 2_Hoc_vien_chia_se\
│   │   └── 3_Clip_ngan_can_xem\
│   ├── Vong_2_Chieu_14h53-17h09\ ...
│   └── Vong_3_Toi_19h12-20h02\ ...
├── Ngay_2_26-09-2026\
│   ├── Vong_1_Sang_08h44-09h10\
│   ├── Vong_2_Trua_11h05-11h31\
│   ├── Vong_3_Chieu_14h39-17h05\
│   └── Vong_4_Toi_18h54-19h31\   (có thêm 4_Anh: ảnh DNG + JPG lúc 18:56)
└── BaoCao_PhanLoai.csv
```

## Đã dựng sẵn trên Google Drive (28/09/2026)

Trong [thư mục Drive của anh](https://drive.google.com/drive/folders/1JvDg1Jxd2HCkJDywry0d1aCpMiLQMTQN) đã có:
- `0_Bang_phan_loai/Bang_phan_loai_video_25-26-09-2026`: Google Sheet 101 dòng. Cột **Xác nhận / Ghi chú** để anh đánh dấu thầy/học viên sau khi xem.
- `Ngay_1_25-09-2026/` với 3 vòng và `Ngay_2_26-09-2026/` với 4 vòng, mỗi vòng đã có sẵn thư mục con (thầy giáo, học viên, clip ngắn, ảnh).

Các thư mục đang **trống**, vì video còn nằm trên thẻ nhớ. Khi chạy `ChayNhanh.bat`, anh nhập thư mục đích là thư mục này trong ổ Google Drive (`G:\My Drive\<tên thư mục>`). Script sẽ chép video vào đúng các thư mục đã có sẵn.

## Bảng vòng

| Ngày | Vòng | Buổi | Giờ quay | Số file | Tổng thời lượng ước tính |
|---|---|---|---|---:|---:|
| 1 · 25/09 | 1 | Sáng | 09:11 – 12:51 | 10 | ~88 phút |
| 1 · 25/09 | 2 | Chiều | 14:53 – 17:09 | 18 | ~52 phút |
| 1 · 25/09 | 3 | Tối | 19:12 – 20:02 | 25 | ~40 phút |
| 2 · 26/09 | 1 | Sáng | 08:44 – 09:10 | 7 | ~27 phút |
| 2 · 26/09 | 2 | Trưa | 11:05 – 11:31 | 11 | ~35 phút |
| 2 · 26/09 | 3 | Chiều | 14:39 – 17:05 | 16 | ~31 phút |
| 2 · 26/09 | 4 | Tối | 18:54 – 19:31 | 14 (12 video + 2 ảnh) | ~34 phút |

Ngày 2 có 5 cụm giờ quay: 08h44, 11h05, 14h39, 16h54 và 18h54. Để ra đúng 4 vòng, cụm 14h39 và cụm 16h54 được gộp thành vòng Chiều, giống cách chia buổi chiều ngày 1. Nếu vòng thực tế khác, sửa cột `Vong` và `ThuMucVong` trong `phan-loai.csv`.

## Thầy giáo / học viên: đây là **bản đoán**, cần xác nhận

Em không xem được nội dung video, nên cột `PhanLoai` trong `phan-loai.csv` được **đoán theo thời lượng**:

- **T · Thầy giáo** (quay liền từ 8 phút trở lên): 0136 (56 phút), 0145, 0193, 0205, 0229, 0230
- **H · Học viên** (từ 30 giây đến dưới 8 phút): phần lớn các clip 1–4 phút, mỗi clip là một lượt chia sẻ
- **K · Clip rất ngắn** (dưới 30 giây, dễ là bấm nhầm hoặc quay thử): 0138, 0149, 0158, 0163, 0164, 0165, 0172, 0180, 0195, 0233, 0234
- **A · Ảnh**: 0223 (DNG + JPG)

Thời lượng được tính từ dung lượng file. Mốc so sánh là file 0136: 15 GB, quay từ 09:17 tới 10:13, tức khoảng 270 MB/phút.

**Cách sửa:** mở `phan-loai.csv` bằng Excel, đổi chữ ở cột `PhanLoai` (T/H/K/A), lưu lại, rồi chạy lại công cụ. Cách khác là kéo thả file giữa các thư mục ngay trên Google Drive.

## Cách chạy

1. Cài **Google Drive for desktop**. Máy sẽ có ổ `G:\My Drive`.
   Nếu muốn lưu vào thư mục Drive được chia sẻ, bấm chuột phải vào thư mục đó trên web → *Organize → Add shortcut → My Drive*. Thư mục sẽ hiện ở `G:\My Drive\<tên thư mục>`.
2. Cắm thẻ nhớ vào máy, nháy đúp **`ChayNhanh.bat`**, nhập:
   - ổ thẻ nhớ, ví dụ `E:\`
   - thư mục Drive, ví dụ `G:\My Drive\KhoaHoc_25-26_09_2026`
   - `1` để xem trước, `2` để sao chép thật
3. Tổng dung lượng khoảng **81 GB**, nên Google Drive cần đủ dung lượng trống. Việc tải lên sẽ mất nhiều giờ tuỳ tốc độ mạng. Nếu bị ngắt giữa chừng, cứ chạy lại: file đã có sẽ được bỏ qua.

Dữ liệu trên thẻ nhớ **không bị di chuyển hay xoá**.
