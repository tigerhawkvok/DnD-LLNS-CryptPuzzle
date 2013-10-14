@echo off
rem Batch script!
python -i main.py
IF ERRORLEVEL 1 (
IF EXIST C:\Python33\python.exe (
C:\Python33\python.exe -i main.py
) ELSE (
echo "Could not find Python. Please manually edit this file to point to the correct Python executable, or add python.exe to your PATH."
)
)
pause