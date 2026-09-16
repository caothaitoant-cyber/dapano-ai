# dapano-ai

Kho tài liệu, dữ liệu và **hệ thống điều khiển doanh nghiệp** của DAPANO GROUP.

> **Cộng Hưởng Cùng Viên Mãn · Think Kind! · Nghĩ Thiện!**

## Bắt đầu từ đâu

👉 **[`HUONG-DAN-TRIEN-KHAI.md`](./HUONG-DAN-TRIEN-KHAI.md)** — 30 phút đầu tiên để chạy được hệ thống.

## Hệ thống điều khiển: 9 phòng ban — 1 tài khoản — 1 bộ não

```
ANH TOÀN ──► P0 ĐIỀU PHỐI ──► P1…P8 (9 phòng ban, mỗi phòng một sub-agent)
                    │
        ┌───────────┴────────────┐
        ▼                        ▼
   BỘ NÃO CHUNG            KHO DỮ LIỆU CHUNG
   CLAUDE.md + bo-nao/     du-lieu/ (7 bảng CSV)
```

| Thư mục | Nội dung |
|---|---|
| [`CLAUDE.md`](./CLAUDE.md) | **Bộ não chung** — luật nền, bảng định tuyến việc về đúng phòng ban |
| [`bo-nao/`](./bo-nao) | Trí nhớ dài hạn: hồ sơ công ty, chân dung khách, bảng giá, 12 quy tắc vàng, từ điển chỉ số, nhật ký quyết định, phân quyền |
| [`.claude/agents/`](./.claude/agents) | 9 phòng ban: Điều phối · Kinh doanh · Marketing · Thẩm định · Vận hành · Tài chính · Pháp lý · Nhân sự · Dữ liệu |
| [`.claude/commands/`](./.claude/commands) | 6 lệnh nhanh: `/giao-ban` `/khach-moi` `/dinh-gia` `/chien-dich` `/bao-cao-tuan` `/chot-ngay` |
| [`du-lieu/`](./du-lieu) | Kho dữ liệu chung — khách hàng, tương tác, toà nhà, giao dịch, chiến dịch, công việc, thu chi |
| [`cong-cu/dpn.py`](./cong-cu/dpn.py) | Công cụ ghi/đọc dữ liệu — mọi phòng ban ghi qua đây, không sửa tay CSV |
| [`quy-trinh/`](./quy-trinh) | 5 luồng việc liên phòng ban + luật bàn giao |
| [`bao-cao/`](./bao-cao) | Sản phẩm giao ra của các phòng ban |
| [`ke-hoach-tang-qua/`](./ke-hoach-tang-qua) | **Thang Quà Dòng Tiền** — phễu quà 6 tầng cho nhà đầu tư toà nhà dòng tiền tại Hà Nội và TP.HCM |
| [`he-thong-dieu-khien.html`](./he-thong-dieu-khien.html) | Sơ đồ hệ thống một trang, chuẩn nhận diện DAPANO (in/chia sẻ được) |

## Ba lệnh dùng nhiều nhất

```bash
python3 cong-cu/dpn.py tong-quan                                   # bảng điều khiển nhanh
python3 cong-cu/dpn.py them khach-hang ho_ten="Chị Lan" nhom=A      # ghi khách mới
python3 cong-cu/dpn.py xem cong-viec --loc phong_ban=P1             # việc của một phòng
```
