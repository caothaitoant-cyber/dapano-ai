# -*- coding: utf-8 -*-
"""Nghiệm thu Máy Tính Dòng Tiền: đọc công thức thật trong file, tự tính, đối chiếu mô hình độc lập."""
import re, sys, openpyxl

def split_args(s):
    args, depth, cur, q = [], 0, '', False
    for ch in s:
        if ch == '"': q = not q
        if not q:
            if ch == '(': depth += 1
            elif ch == ')': depth -= 1
            elif ch == ',' and depth == 0:
                args.append(cur); cur = ''; continue
        cur += ch
    args.append(cur)
    return args

def conv_if(e):
    """IF(a,b,c) -> ((b) if (a) else (c)) — để nhánh không được chọn không bị tính (giống Excel)."""
    while True:
        m = re.search(r'\bIF\(', e)
        if not m: return e
        start = m.end(); depth = 1; i = start; q = False
        while i < len(e):
            ch = e[i]
            if ch == '"': q = not q
            if not q:
                if ch == '(': depth += 1
                elif ch == ')':
                    depth -= 1
                    if depth == 0: break
            i += 1
        inner = e[start:i]
        a = split_args(inner)
        a = [conv_if(x) for x in a] + ['0']*(3-len(a))
        e = e[:m.start()] + f'(({a[1]}) if ({a[0]}) else ({a[2]}))' + e[i+1:]

def make_xl(inputs):
    def xl(expr, local):
        e = expr.lstrip('=')
        e = re.sub(r"'1\. Nhập liệu'!\$?([A-Z]+)\$?(\d+)", lambda m: repr(inputs.get(m.group(1)+m.group(2), 0.0)), e)
        e = re.sub(r"(?<![A-Z0-9_$!'])\$?([A-N])\$?(\d+)", lambda m: repr(local.get(m.group(1)+m.group(2), 0.0)), e)
        e = e.replace('^', '**').replace('<>', '!=')
        e = re.sub(r'(?<![<>=!])=(?!=)', '==', e)
        e = conv_if(e)
        e = re.sub(r'\bROUND\(', 'RND(', e).replace('MAX(', 'max(').replace('MIN(', 'min(')
        return eval(e, {'RND': lambda x, n=0: round(x, int(n)), 'max': max, 'min': min})
    return xl

def load_inputs(IN):
    d = {}
    for row in IN.iter_rows(min_col=2, max_col=2):
        for c in row:
            if isinstance(c.value, (int, float)): d[c.coordinate] = float(c.value)
    d['B11'] = sum(d.get(f'B{r}', 0) for r in (7, 8, 9, 10))
    d['B15'] = max(0, d['B11'] - d['B14'])
    return d

def run(sheet, first_row, xl, cols='BCDEFGHIJL', seed=None):
    local = dict(seed or {}); out = []
    for n in range(1, 11):
        i = first_row + n - 1; local[f'A{i}'] = float(n)
        for col in cols:
            f = sheet[f'{col}{i}'].value
            if isinstance(f, str) and f.startswith('='): local[f'{col}{i}'] = xl(f, local)
        out.append({c: local.get(f'{c}{i}') for c in cols})
    return out

wb = openpyxl.load_workbook('ke-hoach-tang-qua/tang-1/may-tinh-dong-tien.xlsx')
IN, R, S = wb['1. Nhập liệu'], wb['2. Kết quả 10 năm'], wb['3. Ba kịch bản']
inputs = load_inputs(IN); xl = make_xl(inputs)
fails = []

rows = run(R, 15, xl)
print("SHEET 2 · KẾT QUẢ 10 NĂM")
print(" Năm |  Doanh thu |    NOI |  Trả nợ | Dòng tiền | DSCR | Luỹ kế")
for n, r in enumerate(rows, 1):
    d = r['E']/r['I'] if r['I'] > 0 else 0
    print(f" {n:3d} | {r['B']:10,.0f} | {r['E']:6,.0f} | {r['I']:7,.0f} | {r['J']:9,.0f} | {d:4.2f} | {r['L']:7,.0f}")

tv, vay = inputs['B11'], inputs['B15']; goc = vay/inputs['B19']; luy = 0
for n in range(1, 11):
    dt = round(inputs['B22']*max(0, 12-inputs['B23'])*(1+inputs['B28'])**(n-1))
    cp = round(inputs['B24']*12*(1+inputs['B29'])**(n-1)); th = round(dt*inputs['B25'])
    noi = dt-cp-th; dd = max(0, vay-goc*(n-1)); tg = min(goc, dd)
    lai = round((dd+(dd-tg))/2*(inputs['B17'] if n == 1 else inputs['B18']))
    tra = tg+lai; j = noi-tra; luy += j; r = rows[n-1]
    for name, a, b in [('NOI', r['E'], noi), ('Trả nợ', r['I'], tra), ('Dòng tiền', r['J'], j), ('Luỹ kế', r['L'], luy)]:
        if abs(a-b) > 0.51: fails.append(f"Sheet2 năm {n} {name}: file {a:,.1f} ≠ mô hình {b:,.1f}")
print(f"\nCap Rate/tổng vốn năm 1 {rows[0]['E']/tv:.2%} · DSCR {rows[0]['E']/rows[0]['I']:.2f} "
      f"· dòng tiền {rows[0]['J']/12:,.1f} tr/tháng · luỹ kế 10 năm {rows[-1]['L']:,.0f} tr")

print("\nSHEET 3 · BA KỊCH BẢN")
seed = {}
for r_ in range(6, 10):
    for col in 'BCD':
        v = S[f'{col}{r_}'].value
        seed[f'{col}{r_}'] = xl(v, {}) if isinstance(v, str) and v.startswith('=') else float(v)
res = {}
for start, name in [(14, 'THẬN TRỌNG'), (28, 'CƠ SỞ'), (42, 'KỲ VỌNG')]:
    br = run(S, start, xl, cols='BCDEFGHIJ', seed=seed)
    d1 = br[0]['E']/br[0]['I'] if br[0]['I'] > 0 else 0
    tot = sum(r['J'] for r in br); res[name] = (br[0]['J'], d1, tot)
    print(f" · {name:11s}: năm 1 {br[0]['J']:7,.0f} tr ({br[0]['J']/12:5,.1f} tr/th) · DSCR {d1:.2f} · tổng 10 năm {tot:8,.0f} tr")
if not (res['THẬN TRỌNG'][2] < res['CƠ SỞ'][2] < res['KỲ VỌNG'][2]):
    fails.append("Ba kịch bản không xếp đúng thứ tự thận trọng < cơ sở < kỳ vọng")
if abs(res['CƠ SỞ'][0] - rows[0]['J']) > 0.51:
    fails.append(f"Kịch bản CƠ SỞ ({res['CƠ SỞ'][0]:,.0f}) không khớp Sheet 2 ({rows[0]['J']:,.0f})")

empty = {k: 0.0 for k in inputs}
try:
    r0 = run(R, 15, make_xl(empty))
    print(f"\nÔ rỗng (mọi đầu vào = 0): không lỗi chia 0, dòng tiền năm 1 = {r0[0]['J']:,.0f}")
except Exception as ex:
    fails.append(f"Lỗi khi ô rỗng: {ex}")

print()
if fails:
    print("❌ NGHIỆM THU KHÔNG ĐẠT:"); [print("   -", f) for f in fails]; sys.exit(1)
print("✅ NGHIỆM THU ĐẠT — công thức khớp mô hình độc lập, ba kịch bản xếp đúng thứ tự, ô rỗng không vỡ file.")
