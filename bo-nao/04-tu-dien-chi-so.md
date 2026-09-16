# 04 · TỪ ĐIỂN CHỈ SỐ (mọi phòng ban dùng chung một định nghĩa)

> Nếu hai phòng ban tính cùng một chỉ số ra hai số khác nhau, lỗi nằm ở file này chứ không phải
> ở người tính. Sửa định nghĩa ở đây, đừng sửa trong báo cáo.

## A · Chỉ số bất động sản (chuẩn IVS 105 — skill `bds-cashflow-valuation` là nguồn gốc)

| Chỉ số | Công thức | Ngưỡng DAPANO |
|---|---|---|
| **GPR** — Tổng thu thuê tiềm năng | Giá thuê thị trường × 12 × số căn/diện tích | — |
| **EGI** — Thu thực tế | GPR × Tỷ lệ lấp đầy − thất thu | — |
| **NOI** — Thu nhập ròng vận hành | EGI − Chi phí vận hành (**chưa trừ lãi vay, chưa trừ khấu hao**) | — |
| **Cap Rate năm 1** | NOI năm 1 ÷ Tổng vốn đầu tư | ‹điền ngưỡng chấp nhận› — dưới ngưỡng thì **từ chối**, không thương lượng |
| **DSCR** — Khả năng trả nợ | NOI ÷ (Gốc + Lãi phải trả trong năm) | < 1,2 → cảnh báo đỏ |
| **Cash-on-Cash** | Dòng tiền ròng sau nợ ÷ Vốn tự có | — |
| **NPV / IRR** | Chiết khấu dòng tiền theo Discount Rate | NPV < 0 → không mua ở giá đó |
| **Trần giá mua** | Giá cao nhất còn giữ được Cap Rate sàn + DSCR ≥ 1,2 | Con số cuối cùng gửi khách |

**Bắt buộc 3 kịch bản:** Thận trọng · Cơ sở · Kỳ vọng. Không bao giờ gửi khách một con số trần trụi.

## B · Chỉ số kinh doanh

| Chỉ số | Định nghĩa | Nguồn dữ liệu | Cảnh báo |
|---|---|---|---|
| **Lead mới** | Số dòng thêm vào `khach-hang.csv` trong kỳ | `du-lieu/khach-hang.csv` | < ‹điền›/tuần |
| **Lead nóng** | Khách đang ở Bước 5–6 của 8+2 | cột `buoc_8_2` | |
| **Tỷ lệ chuyển đổi** | Số hợp đồng ÷ Số lead cùng nguồn | `giao-dich.csv` | |
| **Thời gian chín** | Ngày từ lead → hợp đồng | 2 file trên | > ‹điền› ngày → soi lại Bước 4 |
| **Khách nguội** | Không tương tác > 14 ngày mà chưa đóng | `tuong-tac.csv` | Kích hoạt lại |
| **Hồ sơ thẩm định tháng** | Số báo cáo Tầng 2 đã trả | `cong-viec.csv` | Trần cứng **30** |
| **Tỷ lệ giới thiệu** | Khách mới đến từ khách cũ ÷ tổng lead | `khach-hang.csv` cột `nguon` | Đây là thước đo chữ **Tín** |

## C · Chỉ số marketing

| Chỉ số | Định nghĩa | Nguồn |
|---|---|---|
| **Quà phát ra** | Số lượt tải theo từng tầng quà | `chien-dich.csv` |
| **Chi phí / lead** | Tổng chi chiến dịch ÷ lead thu được | `chien-dich.csv` + `thu-chi.csv` |
| **Tỷ lệ lên tầng** | Khách tầng N lên tầng N+1 | `khach-hang.csv` cột `tang_qua` |

## D · Chỉ số tài chính công ty

| Chỉ số | Định nghĩa | Nguồn |
|---|---|---|
| **Dòng tiền ròng tháng** | Thu − Chi trong tháng | `thu-chi.csv` |
| **Công nợ phải thu** | Đã ký chưa thu | `giao-dich.csv` |
| **Số tháng sống được** | Tiền mặt ÷ Chi phí cố định tháng | `thu-chi.csv` |

> Chỉ số nào chưa có ngưỡng `‹điền›` thì phòng Dữ liệu vẫn báo con số, kèm dòng chữ
> *"chưa có ngưỡng — cần anh Toàn chốt"*.
