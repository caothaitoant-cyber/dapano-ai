# Mô hình tài chính nhà 7 Lê Văn Linh - đơn vị: triệu VND/tháng
LEASE=90
TAX=0.10   # 5% GTGT + 5% TNCN trên doanh thu (hộ kinh doanh cho thuê), nếu kê khai đầy đủ
VAC=0.08   # trống phòng dài hạn

def longterm(t1, rooms, price, floors_whole=0, floor_price=0, opex=8, capex=0, lease=LEASE, label=""):
    rooms_rev = rooms*price*(1-VAC)
    gross = t1 + rooms_rev + floors_whole*floor_price
    tax = gross*TAX
    net_pre = gross - lease - opex
    net = net_pre - tax
    be = gross - opex - tax   # giá thuê hòa vốn
    return dict(label=label, gross=gross, opex=opex, tax=tax, net_pre=net_pre, net=net, be=be, capex=capex,
                payback=(capex/net if net>0 else None))

def shortstay(t1, rooms, adr, occ, ota=0.15, opex=35, capex=0, lease=LEASE, label=""):
    rooms_gross = rooms*adr*occ*30/1000
    rooms_net = rooms_gross*(1-ota)
    gross = t1 + rooms_net
    tax = gross*TAX
    net_pre = gross - lease - opex
    net = net_pre - tax
    be = gross - opex - tax
    return dict(label=label, gross=gross, opex=opex, tax=tax, net_pre=net_pre, net=net, be=be, capex=capex,
                payback=(capex/net if net>0 else None), rooms_gross=rooms_gross)

rows=[]
# A: hiện trạng - T1 40, T4 2 phòng khép kín 7, 8 phòng không khép kín 3.5
a1=longterm(40, 2, 7, opex=8, label="A. Hiện trạng - phòng khép kín")
a2=longterm(0, 8, 3.5, opex=0, lease=0)
A=dict(label="A. Giữ hiện trạng, cho thuê phòng ngay", gross=a1['gross']+a2['gross'], opex=8, capex=30)
A['tax']=A['gross']*TAX; A['net_pre']=A['gross']-LEASE-A['opex']; A['net']=A['net_pre']-A['tax']; A['be']=A['gross']-A['opex']-A['tax']; A['payback']=None
rows.append(A)
# B: cải tạo 4 tầng chưa khép kín -> 10 phòng khép kín 7tr, T1 42
rows.append(longterm(42, 10, 7, opex=10, capex=340, label="B. Cải tạo khép kín toàn bộ, thuê dài hạn"))
# C: T1+T2 F&B 58, T3 nguyên tầng dịch vụ 15, T4-T6 6 phòng khép kín 7
rows.append(longterm(58, 6, 7, floors_whole=1, floor_price=15, opex=8, capex=190, label="C. Lai: F&B 2 tầng + tầng dịch vụ + 6 phòng khép kín"))
# D: T1+T2 F&B 58, T3-T6 8 phòng lưu trú ngắn ngày
rows.append(shortstay(58, 8, 650, 0.60, opex=35, capex=610, label="D1. Homestay 8 phòng - ADR 650k, lấp đầy 60%"))
rows.append(shortstay(58, 8, 700, 0.65, opex=35, capex=610, label="D2. Homestay 8 phòng - ADR 700k, lấp đầy 65%"))
rows.append(shortstay(58, 8, 800, 0.70, opex=36, capex=610, label="D3. Homestay 8 phòng - ADR 800k, lấp đầy 70%"))

print(f"{'Phương án':60} {'DT':>6} {'Opex':>5} {'Thuế':>5} {'Lãi trc thuế':>12} {'Lãi sau thuế':>12} {'Thuê hòa vốn':>12} {'Capex':>6} {'Hoàn vốn(th)':>12}")
for r in rows:
    pb = f"{r['payback']:.0f}" if r['payback'] else "-"
    print(f"{r['label']:60} {r['gross']:6.1f} {r['opex']:5.0f} {r['tax']:5.1f} {r['net_pre']:12.1f} {r['net']:12.1f} {r['be']:12.1f} {r['capex']:6.0f} {pb:>12}")

print("\nĐộ nhạy theo giá thuê gốc (lãi sau thuế, triệu/tháng):")
for lease in (75,80,85,90):
    c=longterm(58,6,7,floors_whole=1,floor_price=15,opex=8,lease=lease)
    d=shortstay(58,8,700,0.65,opex=35,lease=lease)
    b=longterm(42,10,7,opex=10,lease=lease)
    print(f"  Thuê {lease}: B={b['net']:5.1f}  C={c['net']:5.1f}  D2={d['net']:5.1f}")

print("\nĐộ nhạy homestay (lãi sau thuế) ADR x lấp đầy, thuê 90:")
for adr in (550,650,750,850):
    line=[]
    for occ in (0.5,0.6,0.7,0.8):
        d=shortstay(58,8,adr,occ,opex=35)
        line.append(f"{d['net']:6.1f}")
    print(f"  ADR {adr}k: "+"  ".join(line))
