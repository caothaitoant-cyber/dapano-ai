@echo off
chcp 65001 >nul
echo ==========================================
echo   SAP XEP DU LIEU THE NHO THEO VONG / NGAY
echo ==========================================
echo.
set /p NGUON=O the nho / thu muc goc (vd E:\):
set /p DICH=Thu muc luu ket qua (vd D:\DuLieuDaSapXep):
echo.
echo 1 = Xem truoc (chua sao chep)    2 = Sao chep that
set /p CHON=Chon 1 hoac 2:
if "%CHON%"=="1" (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0SapXepTheoNgay.ps1" -Nguon "%NGUON%" -Dich "%DICH%" -XemTruoc
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0SapXepTheoNgay.ps1" -Nguon "%NGUON%" -Dich "%DICH%"
)
echo.
pause
