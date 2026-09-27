@echo off
chcp 65001 >nul
echo ==================================================
echo   KHOA HOC 25-26/09/2026: THE NHO -^> GOOGLE DRIVE
echo ==================================================
echo.
set /p NGUON=O the nho (vd E:\): 
set /p DICH=Thu muc tren Google Drive (vd G:\My Drive\KhoaHoc_25-26_09_2026): 
echo.
echo 1 = Xem truoc (chua sao chep)    2 = Sao chep that
set /p CHON=Chon 1 hoac 2: 
if "%CHON%"=="1" (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0DuaLenDrive.ps1" -Nguon "%NGUON%" -Dich "%DICH%" -XemTruoc
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0DuaLenDrive.ps1" -Nguon "%NGUON%" -Dich "%DICH%"
)
echo.
pause
