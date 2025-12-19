@echo off
echo ========================================
echo   Ride Fare Estimation Web Application
echo ========================================
echo.
echo This will start both backend and frontend
echo.

cd /d "%~dp0"

echo [1/2] Starting Backend Server...
echo.
start "Ride Fare Backend" cmd /k "cd /d "%~dp0backend" && echo Installing dependencies... && pip install -r requirements.txt >nul 2>&1 && echo Starting FastAPI server... && echo Backend: http://localhost:8000 && echo API Docs: http://localhost:8000/docs && echo. && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

echo Waiting for backend to start...
echo Waiting for backend to start...
ping 127.0.0.1 -n 6 >nul

echo.
echo [2/2] Opening Frontend...
echo.
start "" "%~dp0frontend\index.html"

echo.
echo ========================================
echo   Project Started Successfully! 
echo ========================================
echo.
echo Backend Server: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo Frontend: Opened in your browser
echo.
echo To stop the backend, close the backend terminal window
echo ========================================
echo.

pause
