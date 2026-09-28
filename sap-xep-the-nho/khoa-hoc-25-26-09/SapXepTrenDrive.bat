@echo off
chcp 65001 >nul
set "THUMUC=G:\My Drive\BRIAN SECOND 2\cashflow"
echo ==================================================
echo   SAP XEP VIDEO DA CO TREN GOOGLE DRIVE
echo   %THUMUC%
echo ==================================================
echo.
echo Buoc 1: XEM TRUOC (chua di chuyen file nao)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0DuaLenDrive.ps1" -Nguon "%THUMUC%" -Dich "%THUMUC%" -DiChuyen -XemTruoc
echo.
set /p OK=Dung roi? Go Y de di chuyen that, phim khac de thoat: 
if /i not "%OK%"=="Y" goto :eof
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0DuaLenDrive.ps1" -Nguon "%THUMUC%" -Dich "%THUMUC%" -DiChuyen
echo.
pause
