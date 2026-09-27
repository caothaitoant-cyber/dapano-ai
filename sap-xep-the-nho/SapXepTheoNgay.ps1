<#
.SYNOPSIS
  Sap xep du lieu goc (anh, video, tai lieu) tren the nho theo VONG va theo NGAY.

.DESCRIPTION
  - Doc thoi gian GOC cua tung file, theo thu tu uu tien:
      1. Ngay chup EXIF (anh JPG/PNG/TIFF)
      2. Ngay quay / ngay chup do Windows doc duoc (video MP4/MOV, anh HEIC...)
      3. Ngay sua file (LastWriteTime) - tren the nho day thuong chinh la luc tao file
  - Gom cac ngay thanh tung VONG:
      * Mac dinh: cac ngay lien nhau la cung 1 vong; cach nhau hon -KhoangCachNgay ngay thi sang vong moi.
      * Hoac dung file lich vong (-LichVong) dang CSV: Vong,TuNgay,DenNgay
  - SAO CHEP (khong di chuyen, khong xoa) file sang thu muc dich:
      <Dich>\Vong_01 (2026-09-01 den 2026-09-03)\2026-09-01\20260901_083015_IMG_0001.JPG
  - Xuat bao cao Excel (CSV UTF-8): BaoCao_ChiTiet.csv va BaoCao_TongHop.csv

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\SapXepTheoNgay.ps1 -Nguon E:\ -Dich D:\DuLieuDaSapXep

.EXAMPLE
  # Chi xem truoc, khong sao chep file nao
  powershell -ExecutionPolicy Bypass -File .\SapXepTheoNgay.ps1 -Nguon E:\ -Dich D:\DuLieuDaSapXep -XemTruoc
#>
[CmdletBinding()]
param(
    [string]$Nguon,
    [string]$Dich,
    [int]$KhoangCachNgay = 1,
    [string]$LichVong,
    [switch]$XemTruoc,
    [switch]$GiuTenGoc
)

$ErrorActionPreference = 'Stop'

# ---------- Hoi duong dan neu chua truyen vao ----------
if (-not $Nguon) { $Nguon = Read-Host 'Nhap o the nho / thu muc du lieu goc (vi du E:\)' }
if (-not $Dich)  { $Dich  = Read-Host 'Nhap thu muc luu ket qua (vi du D:\DuLieuDaSapXep)' }
$Nguon = $Nguon.Trim('"', ' ')
$Dich  = $Dich.Trim('"', ' ')

if (-not (Test-Path -LiteralPath $Nguon)) { throw "Khong tim thay thu muc nguon: $Nguon" }
$Nguon = (Resolve-Path -LiteralPath $Nguon).ProviderPath
$DichDay = [System.IO.Path]::GetFullPath($Dich)
if ($DichDay.TrimEnd('\').StartsWith($Nguon.TrimEnd('\'), [System.StringComparison]::OrdinalIgnoreCase) -and
    $DichDay.TrimEnd('\').Length -gt $Nguon.TrimEnd('\').Length) {
    throw 'Thu muc ket qua khong duoc nam ben trong thu muc nguon. Hay chon o/thu muc khac.'
}

# Bo qua file he thong cua the nho / Windows
$BoQuaThuMuc = @('System Volume Information', '$RECYCLE.BIN', 'MISC', '.Trashes', '.Spotlight-V100', '.fseventsd')
$BoQuaFile   = @('Thumbs.db', 'desktop.ini', '.DS_Store')
$BoQuaDuoi   = @('.thm', '.ctg', '.lrv', '.bin', '.dat', '.ind')

# ---------- Doc thoi gian goc ----------
try { Add-Type -AssemblyName System.Drawing } catch { }
$Shell = $null
try { $Shell = New-Object -ComObject Shell.Application } catch { }
$DuoiAnhExif = @('.jpg', '.jpeg', '.tif', '.tiff', '.png')

function Get-NgayExif([string]$DuongDan) {
    $fs = $null; $img = $null
    try {
        $fs  = [System.IO.File]::OpenRead($DuongDan)
        $img = [System.Drawing.Image]::FromStream($fs, $false, $false)
        foreach ($id in 0x9003, 0x9004, 0x0132) {   # DateTimeOriginal, DateTimeDigitized, DateTime
            if ($img.PropertyIdList -contains $id) {
                $s = [System.Text.Encoding]::ASCII.GetString($img.GetPropertyItem($id).Value).Trim([char]0, ' ')
                $d = [datetime]::MinValue
                if ([datetime]::TryParseExact($s, 'yyyy:MM:dd HH:mm:ss', [Globalization.CultureInfo]::InvariantCulture,
                        [Globalization.DateTimeStyles]::None, [ref]$d) -and $d.Year -gt 1990) {
                    return $d
                }
            }
        }
    } catch { } finally {
        if ($img) { $img.Dispose() }
        if ($fs)  { $fs.Dispose() }
    }
    return $null
}

function Get-NgayShell([System.IO.FileInfo]$File) {
    if (-not $Shell) { return $null }
    try {
        $item = $Shell.Namespace($File.DirectoryName).ParseName($File.Name)
        foreach ($p in 'System.Photo.DateTaken', 'System.Media.DateEncoded') {
            $v = $item.ExtendedProperty($p)
            if ($v) {
                $d = [datetime]$v
                if ($d.Year -gt 1990) {
                    if ($d.Kind -ne [DateTimeKind]::Local) { $d = $d.ToLocalTime() }
                    return $d
                }
            }
        }
    } catch { }
    return $null
}

function Get-ThoiGianGoc([System.IO.FileInfo]$File) {
    if ($DuoiAnhExif -contains $File.Extension.ToLower()) {
        $d = Get-NgayExif $File.FullName
        if ($d) { return @($d, 'EXIF ngay chup') }
    }
    $d = Get-NgayShell $File
    if ($d) { return @($d, 'Ngay chup/quay (Windows)') }
    return @($File.LastWriteTime, 'Ngay sua file')
}

# ---------- Quet file ----------
Write-Host ''
Write-Host "Dang quet: $Nguon ..." -ForegroundColor Cyan
$TatCaFile = Get-ChildItem -LiteralPath $Nguon -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object {
    $rel = $_.FullName.Substring($Nguon.Length)
    $trongThuMucBoQua = $false
    foreach ($t in $BoQuaThuMuc) { if ($rel -like "*$t*") { $trongThuMucBoQua = $true; break } }
    -not $trongThuMucBoQua -and
    ($BoQuaFile -notcontains $_.Name) -and
    ($BoQuaDuoi -notcontains $_.Extension.ToLower()) -and
    -not $_.Name.StartsWith('._')
}
$TatCaFile = @($TatCaFile)
if ($TatCaFile.Count -eq 0) { throw 'Khong tim thay file nao trong thu muc nguon.' }

$DanhSach = New-Object System.Collections.Generic.List[object]
$i = 0
foreach ($f in $TatCaFile) {
    $i++
    Write-Progress -Activity 'Doc thoi gian goc' -Status "$i / $($TatCaFile.Count): $($f.Name)" -PercentComplete ($i * 100 / $TatCaFile.Count)
    $kq = Get-ThoiGianGoc $f
    $DanhSach.Add([pscustomobject]@{ File = $f; ThoiGian = $kq[0]; Nguon = $kq[1] })
}
Write-Progress -Activity 'Doc thoi gian goc' -Completed
$DanhSach = @($DanhSach | Sort-Object ThoiGian, { $_.File.Name })

# ---------- Chia vong ----------
$CacNgay = @($DanhSach | ForEach-Object { $_.ThoiGian.Date } | Sort-Object -Unique)
$VongCuaNgay = @{}   # 'yyyy-MM-dd' -> ten vong

if ($LichVong) {
    if (-not (Test-Path -LiteralPath $LichVong)) { throw "Khong tim thay file lich vong: $LichVong" }
    $Lich = @(Import-Csv -LiteralPath $LichVong)
    foreach ($ngay in $CacNgay) {
        $ten = 'Ngoai_lich_vong'
        foreach ($v in $Lich) {
            $tu  = [datetime]::ParseExact($v.TuNgay.Trim(),  'yyyy-MM-dd', $null)
            $den = [datetime]::ParseExact($v.DenNgay.Trim(), 'yyyy-MM-dd', $null)
            if ($ngay -ge $tu -and $ngay -le $den) {
                $ten = "Vong_{0} ({1} den {2})" -f $v.Vong.Trim(), $tu.ToString('yyyy-MM-dd'), $den.ToString('yyyy-MM-dd')
                break
            }
        }
        $VongCuaNgay[$ngay.ToString('yyyy-MM-dd')] = $ten
    }
} else {
    $nhom = @(); $cacNhom = New-Object System.Collections.Generic.List[object]
    foreach ($ngay in $CacNgay) {
        if ($nhom.Count -gt 0 -and ($ngay - $nhom[-1]).TotalDays -gt $KhoangCachNgay) {
            $cacNhom.Add($nhom); $nhom = @()
        }
        $nhom += $ngay
    }
    if ($nhom.Count -gt 0) { $cacNhom.Add($nhom) }
    $so = 0
    foreach ($g in $cacNhom) {
        $so++
        $ten = if ($g[0] -eq $g[-1]) { "Vong_{0:D2} ({1})" -f $so, $g[0].ToString('yyyy-MM-dd') }
               else { "Vong_{0:D2} ({1} den {2})" -f $so, $g[0].ToString('yyyy-MM-dd'), $g[-1].ToString('yyyy-MM-dd') }
        foreach ($n in $g) { $VongCuaNgay[$n.ToString('yyyy-MM-dd')] = $ten }
    }
}

# ---------- Sao chep + bao cao ----------
if (-not $XemTruoc) { New-Item -ItemType Directory -Path $DichDay -Force | Out-Null }
$DaDung = @{}
$ChiTiet = New-Object System.Collections.Generic.List[object]
$stt = 0
foreach ($x in $DanhSach) {
    $stt++
    $ngayStr = $x.ThoiGian.ToString('yyyy-MM-dd')
    $vong    = $VongCuaNgay[$ngayStr]
    $thuMuc  = Join-Path (Join-Path $DichDay $vong) $ngayStr

    $goc  = [System.IO.Path]::GetFileNameWithoutExtension($x.File.Name)
    $duoi = $x.File.Extension
    $tenMoi = if ($GiuTenGoc) { "$goc$duoi" } else { '{0}_{1}{2}' -f $x.ThoiGian.ToString('yyyyMMdd_HHmmss'), $goc, $duoi }
    $dich = Join-Path $thuMuc $tenMoi
    $n = 1
    while ($DaDung.ContainsKey($dich.ToLower()) -or (-not $XemTruoc -and (Test-Path -LiteralPath $dich))) {
        $tenMoi = if ($GiuTenGoc) { "{0}_{1}{2}" -f $goc, $n, $duoi } else { '{0}_{1}_{2}{3}' -f $x.ThoiGian.ToString('yyyyMMdd_HHmmss'), $goc, $n, $duoi }
        $dich = Join-Path $thuMuc $tenMoi
        $n++
    }
    $DaDung[$dich.ToLower()] = $true

    if (-not $XemTruoc) {
        New-Item -ItemType Directory -Path $thuMuc -Force | Out-Null
        Copy-Item -LiteralPath $x.File.FullName -Destination $dich
        (Get-Item -LiteralPath $dich).LastWriteTime = $x.File.LastWriteTime
    }

    $ChiTiet.Add([pscustomobject][ordered]@{
        'STT'             = $stt
        'Vong'            = $vong
        'Ngay'            = $ngayStr
        'Gio'             = $x.ThoiGian.ToString('HH:mm:ss')
        'Thu'             = $x.ThoiGian.ToString('dddd', [Globalization.CultureInfo]'vi-VN')
        'Loai'            = $duoi.TrimStart('.').ToUpper()
        'Ten moi'         = $tenMoi
        'Ten goc'         = $x.File.Name
        'Duong dan goc'   = $x.File.FullName
        'Nguon thoi gian' = $x.Nguon
        'Dung luong (MB)' = [math]::Round($x.File.Length / 1MB, 2)
    })
}

$TongHop = $ChiTiet | Group-Object Vong, Ngay | ForEach-Object {
    $g = $_.Group
    [pscustomobject][ordered]@{
        'Vong'            = $g[0].Vong
        'Ngay'            = $g[0].Ngay
        'Thu'             = $g[0].Thu
        'So file'         = $g.Count
        'Tu gio'          = ($g | Sort-Object Gio)[0].Gio
        'Den gio'         = ($g | Sort-Object Gio)[-1].Gio
        'Loai file'       = (($g | Group-Object Loai | ForEach-Object { "$($_.Name): $($_.Count)" }) -join ', ')
        'Dung luong (MB)' = [math]::Round(($g | Measure-Object 'Dung luong (MB)' -Sum).Sum, 2)
    }
} | Sort-Object Ngay

$ThuMucBaoCao = if ($XemTruoc) { $PSScriptRoot } else { $DichDay }
$fChiTiet = Join-Path $ThuMucBaoCao 'BaoCao_ChiTiet.csv'
$fTongHop = Join-Path $ThuMucBaoCao 'BaoCao_TongHop.csv'
# UTF-8 co BOM de Excel mo dung tieng Viet
$utf8Bom = New-Object System.Text.UTF8Encoding($true)
[System.IO.File]::WriteAllLines($fChiTiet, [string[]]($ChiTiet | ConvertTo-Csv -NoTypeInformation), $utf8Bom)
[System.IO.File]::WriteAllLines($fTongHop, [string[]]($TongHop | ConvertTo-Csv -NoTypeInformation), $utf8Bom)

# ---------- In ket qua ----------
Write-Host ''
Write-Host '=============== KET QUA ===============' -ForegroundColor Green
$TongHop | Format-Table Vong, Ngay, Thu, 'So file', 'Tu gio', 'Den gio', 'Loai file' -AutoSize | Out-String -Width 250 | Write-Host
$demNguon = $ChiTiet | Group-Object 'Nguon thoi gian' | ForEach-Object { "$($_.Name): $($_.Count)" }
Write-Host ("Tong: {0} file, {1} ngay, {2} vong" -f $ChiTiet.Count, $CacNgay.Count, ($VongCuaNgay.Values | Sort-Object -Unique).Count)
Write-Host ("Nguon thoi gian -> " + ($demNguon -join ' | '))
if ($XemTruoc) {
    Write-Host 'CHE DO XEM TRUOC: chua sao chep file nao.' -ForegroundColor Yellow
} else {
    Write-Host "Da sao chep vao: $DichDay" -ForegroundColor Green
    Write-Host 'Du lieu goc tren the nho KHONG bi thay doi.'
}
Write-Host "Bao cao: $fTongHop"
Write-Host "         $fChiTiet"
