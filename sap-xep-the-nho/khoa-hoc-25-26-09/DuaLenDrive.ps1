<#
.SYNOPSIS
  Sao chep video khoa hoc 25-26/09/2026 tu the nho sang Google Drive,
  xep theo Ngay -> Vong -> Thay giao chia se / Hoc vien chia se.

.DESCRIPTION
  Doc bang phan loai phan-loai.csv (moi dong = 1 file). Cot PhanLoai:
      T = Thay giao chia se      -> 1_Thay_giao_chia_se
      H = Hoc vien chia se       -> 2_Hoc_vien_chia_se
      K = Clip rat ngan (<30s)   -> 3_Clip_ngan_can_xem
      A = Anh                    -> 4_Anh
      (de trong / khac)          -> 0_Chua_phan_loai
  Muon doi phan loai: sua cot PhanLoai trong phan-loai.csv roi chay lai.
  File da co o dich (cung dung luong) se duoc bo qua, nen chay lai bao nhieu lan cung duoc.
  Du lieu tren the nho KHONG bi di chuyen hay xoa.
  Rieng -DiChuyen: dung khi video DA nam tren Google Drive (vi du G:\My Drive\BRIAN SECOND 2\cashflow).
  Khi do file o ngay trong thu muc goc duoc DI CHUYEN vao Ngay/Vong/... (khong ton them dung luong, khong tai lai).

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\DuaLenDrive.ps1 -Nguon "G:\My Drive\BRIAN SECOND 2\cashflow" -Dich "G:\My Drive\BRIAN SECOND 2\cashflow" -DiChuyen -XemTruoc

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\DuaLenDrive.ps1 -Nguon E:\ -Dich "G:\My Drive\KhoaHoc_25-26_09_2026" -XemTruoc
#>
[CmdletBinding()]
param(
    [string]$Nguon,
    [string]$Dich,
    [string]$PhanLoai = (Join-Path $PSScriptRoot 'phan-loai.csv'),
    [switch]$XemTruoc,
    # Video da nam san tren Google Drive: di chuyen (khong sao chep) tu goc thu muc -Nguon vao cac thu muc con
    [switch]$DiChuyen
)

$ErrorActionPreference = 'Stop'

if (-not $Nguon) { $Nguon = Read-Host 'O the nho (vi du E:\)' }
if (-not $Dich)  { $Dich  = Read-Host 'Thu muc Google Drive de luu (vi du G:\My Drive\KhoaHoc_25-26_09_2026)' }
$Nguon = $Nguon.Trim('"', ' ')
$Dich  = $Dich.Trim('"', ' ')
if (-not (Test-Path -LiteralPath $Nguon))    { throw "Khong tim thay the nho: $Nguon" }
if (-not (Test-Path -LiteralPath $PhanLoai)) { throw "Khong tim thay bang phan loai: $PhanLoai" }

$ThuMucLoai = @{
    'T' = '1_Thay_giao_chia_se'
    'H' = '2_Hoc_vien_chia_se'
    'K' = '3_Clip_ngan_can_xem'
    'A' = '4_Anh'
}

# Excel co the luu CSV bang dau ';' tuy cai dat vung mien -> tu nhan dien
$dongDau = Get-Content -LiteralPath $PhanLoai -TotalCount 1
$dau = if ($dongDau -like '*;*') { ';' } else { ',' }
$Bang = @(Import-Csv -LiteralPath $PhanLoai -Delimiter $dau)

Write-Host "Dang quet $Nguon ..." -ForegroundColor Cyan
$TrenThe = @{}
# Che do di chuyen chi lay file nam ngay o goc thu muc (khong dong vao cac thu muc con khac)
$quet = if ($DiChuyen) { Get-ChildItem -LiteralPath $Nguon -File -Force -ErrorAction SilentlyContinue }
        else { Get-ChildItem -LiteralPath $Nguon -Recurse -File -Force -ErrorAction SilentlyContinue }
$quet | ForEach-Object {
    $k = $_.Name.ToLower()
    if (-not $TrenThe.ContainsKey($k)) { $TrenThe[$k] = $_ }
}

$TenViec = if ($DiChuyen) { 'di chuyen' } else { 'sao chep' }
$KetQua = New-Object System.Collections.Generic.List[object]
$thieu = 0; $daCo = 0; $saoChep = 0; $tongMB = 0
$i = 0
foreach ($d in $Bang) {
    $i++
    $f = $TrenThe[$d.TenFile.Trim().ToLower()]
    $ngayTxt = ([datetime]::ParseExact($d.NgayQuay.Trim(), 'yyyy-MM-dd', $null)).ToString('dd-MM-yyyy')
    $loai = $d.PhanLoai.Trim().ToUpper()
    $tenLoai = if ($ThuMucLoai.ContainsKey($loai)) { $ThuMucLoai[$loai] } else { '0_Chua_phan_loai' }
    $thuMucVong = Join-Path (Join-Path $Dich ("Ngay_{0}_{1}" -f $d.Ngay.Trim(), $ngayTxt)) $d.ThuMucVong.Trim()
    $thuMuc = Join-Path $thuMucVong $tenLoai

    $daOCho = Join-Path $thuMuc $d.TenFile.Trim()
    if (-not $f -and (Test-Path -LiteralPath $daOCho)) {
        $trangThai = 'Da co san'
        $daCo++
    } elseif (-not $f) {
        $trangThai = 'KHONG TIM THAY'
        $thieu++
    } else {
        $fileDich = Join-Path $thuMuc $f.Name
        if ((Test-Path -LiteralPath $fileDich) -and (Get-Item -LiteralPath $fileDich).Length -eq $f.Length) {
            $trangThai = 'Da co san'
            $daCo++
        } else {
            $trangThai = if ($XemTruoc) { "Se $TenViec" } else { "Da $TenViec" }
            if (-not $XemTruoc) {
                Write-Progress -Activity 'Sap xep len Google Drive' -Status "$i / $($Bang.Count): $($f.Name) ($([math]::Round($f.Length/1GB,2)) GB)" -PercentComplete ($i * 100 / $Bang.Count)
                foreach ($con in $ThuMucLoai['T'], $ThuMucLoai['H']) {
                    New-Item -ItemType Directory -Path (Join-Path $thuMucVong $con) -Force | Out-Null
                }
                New-Item -ItemType Directory -Path $thuMuc -Force | Out-Null
                if ($DiChuyen) { Move-Item -LiteralPath $f.FullName -Destination $fileDich -Force }
                else           { Copy-Item -LiteralPath $f.FullName -Destination $fileDich -Force }
            }
            $saoChep++
            $tongMB += $f.Length / 1MB
        }
    }
    $KetQua.Add([pscustomobject][ordered]@{
        Ngay = $d.Ngay; Vong = $d.ThuMucVong; PhanLoai = $tenLoai; TenFile = $d.TenFile
        GioBatDau = $d.GioBatDau; ThoiLuongPhut = $d.ThoiLuongPhut; TrangThai = $trangThai
    })
}
Write-Progress -Activity 'Sap xep len Google Drive' -Completed

Write-Host ''
Write-Host '=============== KET QUA ===============' -ForegroundColor Green
$KetQua | Group-Object Ngay, Vong, PhanLoai | ForEach-Object {
    [pscustomobject]@{ 'Ngay / Vong / Phan loai' = $_.Name.Replace(', ', ' / '); 'So file' = $_.Count }
} | Format-Table -AutoSize | Out-String -Width 250 | Write-Host

$verb = if ($XemTruoc) { "Se $TenViec" } else { "Da $TenViec" }
Write-Host ("{0}: {1} file ({2:N1} GB) | Da co san: {3} | Khong tim thay: {4}" -f $verb, $saoChep, ($tongMB / 1024), $daCo, $thieu)
if ($thieu -gt 0) {
    Write-Host 'Cac file khong tim thay (chua tai len xong / chua co tren the):' -ForegroundColor Yellow
    $KetQua | Where-Object TrangThai -eq 'KHONG TIM THAY' | ForEach-Object { Write-Host "  $($_.TenFile)" }
}

$baoCao = if ($XemTruoc) { Join-Path $PSScriptRoot 'BaoCao_XemTruoc.csv' } else { Join-Path $Dich 'BaoCao_PhanLoai.csv' }
$utf8Bom = New-Object System.Text.UTF8Encoding($true)
[System.IO.File]::WriteAllLines($baoCao, [string[]]($KetQua | ConvertTo-Csv -NoTypeInformation), $utf8Bom)
Write-Host "Bao cao: $baoCao"
if ($XemTruoc) { Write-Host "CHE DO XEM TRUOC: chua $TenViec file nao." -ForegroundColor Yellow }
