# 06 · MỘT TÀI KHOẢN — NHIỀU PHÒNG BAN

Anh Toàn dùng **một tài khoản Claude duy nhất** cho cả công ty. Phòng ban được phân chia
bằng **vai trò và quyền hạn trong hệ thống này**, không phải bằng số tài khoản.

## Vì sao một tài khoản lại an toàn hơn nhiều tài khoản

| | Nhiều tài khoản | Một tài khoản + hệ thống này |
|---|---|---|
| Trí nhớ công ty | Mỗi nơi nhớ một kiểu, không ai biết ai đã hứa gì với khách | Một bộ não, mọi phòng ban đọc cùng một sự thật |
| Dữ liệu khách | Rải rác trong máy từng người | Một kho `du-lieu/`, có lịch sử Git |
| Người nghỉ việc | Mang theo dữ liệu | Dữ liệu ở lại repo, người đi không mang được |
| Chi phí | Nhân lên theo đầu người | Một gói |
| Kiểm soát | Không ai soi được ai | Mọi thay đổi đều có commit, ai sửa gì đều thấy |

## Bốn lớp kiểm soát thay cho việc chia tài khoản

**Lớp 1 — Vai trò.** Mỗi phòng ban là một file trong `.claude/agents/` ghi rõ: được làm gì,
không được làm gì, đọc file nào, ghi file nào.

**Lớp 2 — Quyền công cụ.** File `.claude/settings.json` chặn sẵn những lệnh nguy hiểm
(xoá dữ liệu, ép đẩy code, đổi lịch sử).

**Lớp 3 — Dấu vết.** Mọi ghi chép đi qua `cong-cu/dpn.py` → CSV → commit Git. Nhìn lịch sử
là biết ngày nào phòng nào ghi gì.

**Lớp 4 — Bốn việc chỉ anh Toàn quyết.** (Quy tắc vàng số 11): ký hợp đồng · đổi giá · chi tiền ·
đăng công khai.

## Bảng phân quyền chi tiết

| Phòng ban | Được ĐỌC | Được GHI | Phải xin duyệt |
|---|---|---|---|
| P0 Điều phối | Tất cả | `cong-viec.csv`, `05-nhat-ky-quyet-dinh.md` | Thay đổi cấu trúc phòng ban |
| P1 Kinh doanh | Bộ não + khách + toà nhà | `khach-hang.csv`, `tuong-tac.csv`, `cong-viec.csv` | Báo giá ngoài bảng · mọi cam kết |
| P2 Marketing | Bộ não + khách + chiến dịch | `chien-dich.csv`, `bao-cao/`, `cong-viec.csv` | **Đăng bài ra kênh công khai** |
| P3 Thẩm định | Bộ não + toà nhà + khách | `toa-nha.csv`, `bao-cao/`, `cong-viec.csv` | Gửi trần giá mua cho khách |
| P4 Vận hành | Bộ não + khách + giao dịch | `tuong-tac.csv`, `cong-viec.csv` | Cam kết bồi thường/miễn giảm |
| P5 Tài chính | Tất cả số liệu tiền | `thu-chi.csv`, `giao-dich.csv` | **Mọi khoản chi ra ngoài** |
| P6 Pháp lý | Bộ não + giao dịch + toà nhà | `bao-cao/`, `cong-viec.csv` | **Mọi bản hợp đồng cuối** |
| P7 Nhân sự | Bộ não + công việc | `bao-cao/`, `cong-viec.csv` | Tuyển · lương · sa thải |
| P8 Dữ liệu | Tất cả (chỉ đọc) | `bao-cao/` | Không (chỉ báo cáo) |

## Khi có thêm người thật vào công ty

Không cấp tài khoản mới ngay. Làm theo thứ tự:

1. Người đó làm việc **qua anh Toàn** trong 2 tuần đầu — mọi việc đi qua phòng ban tương ứng.
2. Khi đã quen luật, cấp quyền truy cập repo GitHub (chỉ nhánh làm việc, không nhánh chính).
3. Chỉ cấp tài khoản Claude riêng khi người đó **phụ trách trọn một phòng ban** và đã thuộc
   `03-quy-tac-vang.md`. Tài khoản mới vẫn phải trỏ về đúng repo này — bộ não vẫn là một.

## Nguyên tắc bất biến

> **Nhiều cái đầu làm việc — một trí nhớ duy nhất.**
> Ngày nào một phòng ban bắt đầu ghi chép riêng ngoài `du-lieu/`, ngày đó hệ thống bắt đầu hỏng.
