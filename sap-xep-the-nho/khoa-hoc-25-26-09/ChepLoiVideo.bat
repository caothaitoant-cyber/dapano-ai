@echo off
chcp 65001 >nul
setlocal
set "NGUON=G:\My Drive\BRIAN SECOND 2\cashflow"
set "DICH=%USERPROFILE%\Desktop\LoiNoi_KhoaHoc"
set "PYEXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
echo ==================================================
echo   CHEP LOI VIDEO KHOA HOC 25-26/09 (tieng Viet)
echo   Nguon:   %NGUON%
echo   Ket qua: %DICH%\TatCa_LoiNoi.txt
echo ==================================================
echo.

rem --- Tim Python; neu chua co thi tu cai bang winget ---
set "PY="
py -3 -c "import sys" >nul 2>nul && set PY=py -3
if not defined PY python -c "import sys" >nul 2>nul && set PY=python
if not defined PY if exist "%PYEXE%" set PY="%PYEXE%"
if not defined PY (
  echo Chua co Python - dang tu cai dat, vui long doi...
  winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
  if exist "%PYEXE%" set PY="%PYEXE%"
)
if not defined PY (
  echo Khong tu cai duoc Python. Hay cai tu https://www.python.org/downloads/
  echo ^(nho tick "Add python.exe to PATH"^) roi nhay dup lai file nay.
  pause
  exit /b 1
)

echo Dang cai thu vien chep loi ^(chi lau o lan dau^)...
%PY% -m pip install --quiet --upgrade faster-whisper
echo.
echo Bat dau chep loi. Mat khoang 1-3 tieng - cu de may chay.
echo Neu bi ngat, nhay dup lai: video da chep se duoc bo qua.
echo.
%PY% "%~dp0chep_loi.py" "%NGUON%" "%DICH%" --model small
echo.
explorer "%DICH%"
pause
