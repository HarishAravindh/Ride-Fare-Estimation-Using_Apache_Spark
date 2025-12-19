# 🚀 SPARK Project - Quick Start Guide

## What's New: RUN SERVER Button ⚡

You now have a dedicated **RUN SERVER** button in every page of the application!

### Location
- Click **⚡ RUN SERVER** in the sidebar menu (main navigation)
- Opens in a new tab with the SPARK Launcher interface

---

## How to Run the Project

### Option 1: Quick Launch (Recommended)
1. Open any app page (index.html)
2. Click **⚡ RUN SERVER** button in the sidebar
3. This opens the **SPARK Launcher** page with all controls
4. Click the **🚀 Run All** button
5. Copy the command and paste it into your terminal
6. Click **⭐ LAUNCH APP** when servers are ready

### Option 2: Manual Commands
Open PowerShell in your project folder and run:

**Start Everything:**
```powershell
cd "c:\Users\sweth\OneDrive\Documents\Custom Office Templates\SPARK_PROJECT"
start_project.bat
```

**Or start separately:**
```powershell
# Terminal 1 - Backend
start_backend.bat

# Terminal 2 - Frontend
start_frontend.bat
```

---

## What You Get

### Backend Server (Port 8000)
- FastAPI REST API
- Ride fare prediction
- Spark integration
- Real-time visualization data

**Endpoints:**
- `http://localhost:8000/predict` - Fare prediction
- `http://localhost:8000/breakdown` - Fare breakdown
- `http://localhost:8000/demand-supply` - Demand/Supply data
- `http://localhost:8000/stats` - Backend statistics

### Frontend Application
- **index.html** - Main cyberpunk UI (sidebar menu)
- **index_hamburger.html** - Hamburger menu variant
- **index_old.html** - Gradient UI variant
- **launcher.html** - Server control center

### Spark Web UI (Port 4040)
- Monitor Spark jobs
- View running applications
- Check computation metrics

---

## File Locations

```
SPARK_PROJECT/
├── frontend/
│   ├── index.html              ← Main app (sidebar)
│   ├── index_hamburger.html    ← Hamburger variant
│   ├── index_old.html          ← Gradient variant
│   ├── launcher.html           ← RUN SERVER page
│   ├── login.html              ← Authentication
│   ├── register.html           ← New account
│   └── change_password.html    ← Change password
├── backend/
│   ├── main.py                 ← FastAPI server
│   ├── model.py                ← Prediction logic
│   └── spark_session.py        ← Spark setup
├── start_project.bat           ← Run everything
├── start_backend.bat           ← Backend only
├── start_frontend.bat          ← Frontend only
└── stop_backend.bat            ← Stop backend
```

---

## First Time Setup

### 1. Install Python Dependencies
```powershell
cd backend
pip install -r requirements.txt
```

### 2. Ensure Java is Installed (for Spark)
Spark requires Java 8+
```powershell
java -version
```

### 3. Open Frontend
Use any of these:
- `frontend/index.html` (main)
- `frontend/launcher.html` (control center)

### 4. Register/Login
- First time: Click register link on login page
- Create username and password
- Access all features

---

## Features

✅ **Ride Fare Prediction**
- Real-time estimates
- Kilometer-based distance
- Time-based calculations
- Surge pricing (peak hours)
- Weekend multipliers

✅ **Visualizations**
- Fare breakdown (bar chart)
- Demand vs Supply (line chart)
- Sidebar layout

✅ **Spark Integration**
- Distributed computing
- Web UI monitoring
- Sample job execution
- Real-time status

✅ **User Authentication**
- Registration system
- Login validation
- Password change
- LocalStorage security

✅ **Cyberpunk Neon Theme**
- Cyan (#0ff) accents
- Magenta (#f0f) highlights
- Dark background
- Glow effects

---

## Troubleshooting

### Backend won't start
- Check if port 8000 is in use
- Verify Python installation
- Ensure Java is installed (for Spark)

### Frontend shows "Backend not running"
- Make sure `start_backend.bat` is running
- Check if port 8000 is accessible
- Try refreshing the page

### Spark features not working
- Install Java: https://www.java.com/en/download/
- Spark Web UI opens at `http://localhost:4040`
- Check console for error messages

### Stopped working after changes
- Restart the backend server
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)

---

## Quick Commands Reference

| What | Command |
|------|---------|
| Run everything | `start_project.bat` |
| Run backend only | `start_backend.bat` |
| Run frontend only | `start_frontend.bat` |
| Stop backend | `stop_backend.bat` |
| Open launcher | Click **⚡ RUN SERVER** button |
| Access app | `frontend/index.html` |
| Spark Web UI | `http://localhost:4040` |
| Backend API | `http://localhost:8000` |

---

## Support

Need help? Check:
1. Browser console (F12) for errors
2. Terminal output when running servers
3. SPARK Launcher page for status
4. README files in backend/ folder

---

**Made with ❤️ for SPARK Project**
**Last Updated:** December 2025

