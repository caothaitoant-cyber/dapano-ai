# Sắp xếp dữ liệu thẻ nhớ theo Vòng / Ngày

Công cụ chạy trên **Windows**: đọc **thời gian gốc** của từng file trên thẻ nhớ (ảnh, video, tài liệu), rồi **sao chép** sang thư mục mới, xếp theo **Vòng → Ngày**. Kèm theo là bảng báo cáo mở được bằng Excel.

> Dữ liệu gốc trên thẻ nhớ **không bị di chuyển, đổi tên hay xoá**. Công cụ chỉ sao chép.

## Cách dùng nhanh

1. Tải cả thư mục `sap-xep-the-nho` về máy (hoặc chỉ 2 file `SapXepTheoNgay.ps1` và `ChayNhanh.bat`, để chung một thư mục).
2. Cắm thẻ nhớ vào máy và xem thẻ nhận là ổ gì (ví dụ `E:\`).
3. Nháy đúp **`ChayNhanh.bat`** rồi nhập:
   - ổ thẻ nhớ, ví dụ `E:\`
   - thư mục lưu kết quả, ví dụ `D:\DuLieuDaSapXep` (**không** đặt trong thẻ nhớ)
   - `1` để **xem trước**: chưa sao chép gì, chỉ ra bảng báo cáo
   - `2` để **sao chép thật**
4. Mở `BaoCao_TongHop.csv` bằng Excel để xem từng vòng, từng ngày có bao nhiêu file.

> Nếu Windows hiện cảnh báo "Windows protected your PC", bấm **More info → Run anyway**.

## Kết quả

```
D:\DuLieuDaSapXep\
├── Vong_01 (2026-09-01 den 2026-09-02)\
│   ├── 2026-09-01\
│   │   ├── 20260901_083015_IMG_0001.JPG
│   │   └── 20260901_091502_IMG_0002.JPG
│   └── 2026-09-02\
│       └── 20260902_140010_MVI_0003.MP4
├── Vong_02 (2026-09-10 den 2026-09-11)\ ...
├── BaoCao_TongHop.csv    ← mỗi dòng = 1 ngày: vòng, thứ, số file, từ giờ – đến giờ, loại file
└── BaoCao_ChiTiet.csv    ← mỗi dòng = 1 file: tên mới, tên gốc, đường dẫn gốc, nguồn thời gian
```

- **Tên file mới** = `NămThángNgày_GiờPhútGiây_TênGốc`, nên trong mỗi thư mục file tự xếp đúng thứ tự thời gian. Nếu muốn giữ nguyên tên gốc, thêm `-GiuTenGoc` khi chạy.
- Hai file trùng tên (ví dụ thẻ đã reset bộ đếm ảnh) được tự thêm đuôi `_1`, `_2`…, không file nào bị ghi đè.

## Thời gian gốc được lấy thế nào

Theo thứ tự ưu tiên (cột **Nguồn thời gian** trong báo cáo cho biết file nào lấy theo cách nào):

1. **EXIF ngày chụp**: ảnh JPG, PNG, TIFF từ máy ảnh hoặc điện thoại.
2. **Ngày chụp/quay do Windows đọc**: video MP4, MOV, ảnh HEIC…
3. **Ngày sửa file**: dùng khi file không có hai thông tin trên. Trên thẻ nhớ, đây thường chính là lúc file được tạo.

Các file hệ thống của thẻ và Windows (`System Volume Information`, `Thumbs.db`, `.THM`, `.LRV`…) được bỏ qua.

## Cách chia Vòng

**Mặc định (tự động):** các ngày **liền nhau** gộp chung một vòng. Hễ cách nhau từ 2 ngày trở lên thì sang vòng mới.
Muốn gộp các ngày cách nhau xa hơn, ví dụ cách 3 ngày vẫn tính cùng vòng, chạy:

```powershell
powershell -ExecutionPolicy Bypass -File .\SapXepTheoNgay.ps1 -Nguon E:\ -Dich D:\KetQua -KhoangCachNgay 3
```

**Theo lịch vòng có sẵn:** sửa file `lich-vong-mau.csv` (mở bằng Excel hoặc Notepad), mỗi dòng là một vòng, ngày ghi theo dạng `yyyy-MM-dd`:

```
Vong,TuNgay,DenNgay
01,2026-09-01,2026-09-03
02,2026-09-10,2026-09-12
```

rồi chạy:

```powershell
powershell -ExecutionPolicy Bypass -File .\SapXepTheoNgay.ps1 -Nguon E:\ -Dich D:\KetQua -LichVong .\lich-vong-mau.csv
```

File có ngày nằm ngoài mọi vòng sẽ được xếp vào thư mục `Ngoai_lich_vong`, để không file nào bị bỏ sót.

## Tuỳ chọn

| Tham số | Ý nghĩa |
|---|---|
| `-Nguon` | Ổ thẻ nhớ hoặc thư mục dữ liệu gốc |
| `-Dich` | Thư mục lưu kết quả |
| `-XemTruoc` | Chỉ ra báo cáo, chưa sao chép |
| `-KhoangCachNgay N` | Hai ngày cách nhau quá N ngày thì tính là vòng mới (mặc định 1) |
| `-LichVong file.csv` | Chia vòng theo lịch có sẵn |
| `-GiuTenGoc` | Không thêm ngày giờ vào tên file |
