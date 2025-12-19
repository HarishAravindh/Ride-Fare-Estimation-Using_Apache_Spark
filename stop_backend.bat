@echo off
echo ========================================
echo   Stopping Ride Fare Backend Server
echo ========================================
echo.
echo Searching for Python processes running on port 8000...
echo.

for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000 ^| findstr LISTENING') do (
    echo Found process: %%a
    taskkill /F /PID %%a
)

echo.
echo Backend server stopped!
echo ========================================
pause
