---
description: Tiếp nhận một khách mới — ghi CRM, phân nhóm A/B/C, giao việc phòng Kinh doanh
argument-hint: "<tên khách> <sđt> <nguồn> <điều khách nói>"
---

Tiếp nhận khách mới: $ARGUMENTS

Làm đủ 5 việc, không bỏ bước:

1. **Đọc** `bo-nao/01-chan-dung-khach-hang.md`, xác định khách thuộc nhóm **A / B / C**.
   Chưa đủ dữ kiện để phân nhóm thì ghi `nhom=?` và ghi rõ cần hỏi gì thêm — **không đoán**.
2. **Ghi vào CRM**:
   ```bash
   python3 cong-cu/dpn.py them khach-hang ho_ten="…" sdt=… email=… nhom=… nguon=… \
     tang_qua=… buoc_8_2=1 thanh_pho=… trang_thai=moi ghi_chu="nguyên văn điều khách nói"
   ```
3. **Ghi tương tác đầu tiên** vào `tuong-tac.csv` với nguyên văn điều khách nói.
4. **Giao `p1-kinh-doanh`** soạn kịch bản chạm lần đầu theo đúng bước 8+2 mà khách đang đứng,
   kèm món quà đúng tầng cho nhóm khách đó.
5. **Tạo việc theo dõi** với hạn trong 24 giờ:
   ```bash
   python3 cong-cu/dpn.py them cong-viec phong_ban=P1 tieu_de="Chạm lần đầu <tên khách>" \
     lien_quan=KH-00xx uu_tien=cao han=<ngày mai>
   ```

Trả về: mã khách, nhóm, tầng quà đề xuất, kịch bản chạm lần đầu, và mã việc đã tạo.
