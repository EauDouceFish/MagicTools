@echo off
setlocal

if "%1"=="" (
    echo Please provide an IP address.
    exit /b
)

if "%1"=="trt" (
    if "%2"=="" (
        echo Please provide an IP address to trace.
        exit /b
    )
    echo Tracing route to %2...
    tracert %2
    exit /b
)

rem 如果只输入了IP地址
set ip=%1
echo IP Information:
python D:\MagicTools\ip\ip.py %ip%

endlocal
