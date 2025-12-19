@echo off
echo ========================================
echo Starting Ride Fare Estimation Backend
echo ========================================
echo.

cd /d "%~dp0backend"

echo Installing/Updating dependencies...
pip install -r requirements.txt
echo.

echo Starting FastAPI server...
echo Backend will be available at: http://localhost:8000
echo API Documentation at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause
