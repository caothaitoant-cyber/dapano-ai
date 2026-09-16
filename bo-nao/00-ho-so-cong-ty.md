# 00 · HỒ SƠ CÔNG TY

## Danh tính

| Mục | Nội dung |
|---|---|
| Tên | **DAPANO GROUP** |
| Lĩnh vực | Tư vấn & môi giới bất động sản dòng tiền (toà nhà cho thuê), đào tạo nhà đầu tư |
| Slogan VN | **Cộng Hưởng Cùng Viên Mãn** |
| Slogan EN | **Think Kind!** |
| Câu ký | **Nghĩ Thiện!** |
| Triết lý sản phẩm | **Cash Flow First** — dòng tiền quyết định giá trị thật, giá thị trường chỉ là tham chiếu |
| Triết lý kinh doanh | Đầu tư đúng — không chỉ làm giàu cho mình, mà còn nâng đỡ người khác |
| Nền tảng đạo đức | Ngũ thường: **Nhân · Nghĩa · Lễ · Trí · Tín** |
| Thị trường chính | Hà Nội và TP. Hồ Chí Minh |
| Người quyết định cuối | Anh Toàn (chủ tịch) |

## Sản phẩm lõi

1. **Tư vấn – thẩm định – môi giới toà nhà dòng tiền** (giá trị giao dịch 8–50 tỷ).
2. **Đào tạo / coaching nhà đầu tư** — workshop, khảo sát thực địa, mentoring.
3. **Vận hành hộ** toà nhà cho thuê sau khi khách sở hữu.

> Chi tiết gói và giá: xem [`02-san-pham-va-gia.md`](./02-san-pham-va-gia.md).

## Sơ đồ 9 phòng ban

```
                        ┌──────────────────────────┐
                        │   ANH TOÀN · CHỦ TỊCH    │
                        │  (người duyệt cuối cùng) │
                        └────────────┬─────────────┘
                                     │
                        ┌────────────▼─────────────┐
                        │   P0 · ĐIỀU PHỐI         │
                        │   (Chief of Staff)       │
                        │   nhận việc → chia việc  │
                        └────────────┬─────────────┘
        ┌───────────┬────────────┬───┴────┬────────────┬───────────┐
        ▼           ▼            ▼        ▼            ▼           ▼
   P1 KINH     P2 MARKETING  P3 THẨM   P4 VẬN      P5 TÀI      P6 PHÁP
   DOANH       & CONTENT     ĐỊNH      HÀNH        CHÍNH       LÝ
        │           │            │        │            │           │
        └───────────┴────────────┴────┬───┴────────────┴───────────┘
                                      ▼
                         P7 NHÂN SỰ · P8 DỮ LIỆU & BÁO CÁO
                                      │
                         ┌────────────▼─────────────┐
                         │  BỘ NÃO CHUNG  bo-nao/   │
                         │  DỮ LIỆU CHUNG du-lieu/  │
                         └──────────────────────────┘
```

| Mã | Phòng ban | Sản phẩm đầu ra chính | File định nghĩa |
|---|---|---|---|
| P0 | Điều phối | Phân việc, giao ban, nhật ký quyết định | `.claude/agents/p0-dieu-phoi.md` |
| P1 | Kinh doanh | Kịch bản tư vấn 8+2, hồ sơ khách, đề xuất chốt | `.claude/agents/p1-kinh-doanh.md` |
| P2 | Marketing & Content | Post, thư bán hàng, kịch bản video, phễu quà | `.claude/agents/p2-marketing.md` |
| P3 | Thẩm định & Đầu tư | Báo cáo định giá 8 phần, trần giá mua | `.claude/agents/p3-tham-dinh.md` |
| P4 | Vận hành & CSKH | Lịch chăm sóc, xử lý sự vụ toà nhà | `.claude/agents/p4-van-hanh.md` |
| P5 | Tài chính – Kế toán | Dòng tiền công ty, công nợ, hoa hồng | `.claude/agents/p5-tai-chinh.md` |
| P6 | Pháp lý & Hợp đồng | Checklist pháp lý, rà hợp đồng | `.claude/agents/p6-phap-ly.md` |
| P7 | Nhân sự & Đào tạo | Tuyển, onboard, huấn luyện sale | `.claude/agents/p7-nhan-su.md` |
| P8 | Dữ liệu & Báo cáo | Báo cáo ngày/tuần/tháng, cảnh báo chỉ số | `.claude/agents/p8-du-lieu.md` |

## Mục tiêu năm hiện tại

| Chỉ số | Mục tiêu | Ghi chú |
|---|---|---|
| Số giao dịch toà nhà | ‹điền› | |
| Doanh thu môi giới | ‹điền› | |
| Doanh thu đào tạo | ‹điền› | |
| Lead mới / tháng | ‹điền› | |
| Tỷ lệ lead → hợp đồng | ‹điền› | |
| Số hồ sơ thẩm định / tháng | 30 (năng lực thật của đội thẩm định) | Nguồn: `ke-hoach-tang-qua/README.md` Tầng 2 |

## Nhân sự thật

| Vai trò | Tên | Phụ trách phòng ban |
|---|---|---|
| Chủ tịch | Anh Toàn | Duyệt cuối, P0 |
| ‹điền› | ‹điền› | ‹điền› |

> Khi chưa có người thật cho một phòng ban, sub-agent của phòng ban đó vẫn chạy được —
> nó làm việc, ra sản phẩm, và ghi rõ "cần người thật xác nhận" ở cuối báo cáo.
