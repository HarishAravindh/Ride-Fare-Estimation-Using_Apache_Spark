# ⚡ QUICK START GUIDE - SPARK PROJECT

## 🚀 30-Second Setup

### Step 1: Open Launcher
```
frontend/launcher.html
```

### Step 2: Click "🚀 Run All"
- Copy the command
- Paste into PowerShell/Command Prompt
- Press Enter

### Step 3: Wait for Backend Status
- Should show: `✅ Backend is RUNNING`

### Step 4: Click "🔥 START SPARK SESSION"
- Wait 30-60 seconds
- Should show green status indicator

### Step 5: Use the System
- Click "LAUNCH APP" to start using
- Click "Open Spark Web UI" to monitor jobs

---

## 🔥 SPARK UI WEB ADDRESS
```
http://localhost:4040
```
*(Only available after clicking "START SPARK SESSION")*

---

## 📊 LAUNCHER.HTML SECTIONS

### Server Control
- Run All (Backend + Frontend)
- Backend Only
- Frontend Only
- Stop Backend
- Launch App
- Real-time server status

### Spark Management
- Start Spark Session
- Check Spark Status
- Run Sample Job (test)
- Stop Spark Session
- Real-time Spark status
- Open Spark Web UI (when available)

### Commands
- Copy-to-clipboard for all commands
- Direct links to documentation
- FastAPI docs link

---

## 🔧 JAVA SETUP (If Needed)

### Check Java:
```powershell
java -version
echo $env:JAVA_HOME
```

### Install Java:
- Download: https://www.java.com/en/download/
- Or: https://www.oracle.com/java/technologies/downloads/

### Set JAVA_HOME:
```powershell
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Java\jdk-21", "User")
```
*(Replace "jdk-21" with your Java version)*

---

## 🎯 COMMON TASKS

### Start Everything:
1. Open launcher.html
2. Click "Run All"
3. Copy command and run in terminal

### Check Backend Status:
- Launcher shows status automatically
- Refreshes every 5 seconds

### Initialize Spark:
- Click "START SPARK SESSION" button
- Wait for green status indicator

### Monitor Spark Jobs:
- Click "Open Spark Web UI" (http://localhost:4040)
- Runs in real-time

### Stop Everything:
- Click "Stop Backend" in launcher
- Or close the terminal

### Install Dependencies:
```powershell
pip install -r backend/requirements.txt
```

---

## ❌ TROUBLESHOOTING

### Backend Won't Start:
```powershell
# Make sure you're in the right directory
cd "c:\Users\sweth\OneDrive\Documents\Custom Office Templates\SPARK_PROJECT"

# Install dependencies
pip install -r backend/requirements.txt

# Try again
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Spark Won't Start:
1. Check Java: `java -version`
2. Check PySpark: `pip install pyspark`
3. Check JAVA_HOME: `echo $env:JAVA_HOME`
4. Check port 4040: `netstat -ano | findstr :4040`

### Backend Doesn't Appear Running:
- Wait 5-10 seconds (launcher auto-refreshes)
- Manually refresh launcher.html
- Check terminal for error messages

---

## 📍 IMPORTANT URLS

| Purpose | URL |
|---------|-----|
| **Launcher** | `frontend/launcher.html` |
| **Main App** | `frontend/index.html` |
| **Backend API** | `http://localhost:8000` |
| **Backend Docs** | `http://localhost:8000/docs` |
| **Spark Web UI** | `http://localhost:4040` |

---

## 💡 KEY FEATURES

✅ **Real-time Status Updates**
- Shows server and Spark status
- Updates automatically every 5-10 seconds

✅ **One-Click Spark Management**
- Start, stop, check status
- Run test jobs
- Access Web UI

✅ **Comprehensive Error Messages**
- Shows what went wrong
- Provides solutions
- Links to resources

✅ **Copy-to-Clipboard Commands**
- All commands easily copied
- Ready to paste into terminal

✅ **Beautiful Neon UI**
- Cyberpunk theme
- Easy to read status indicators
- Professional design

---

## 🔄 SYSTEM FLOW

```
User Opens launcher.html
         ↓
Checks backend status (auto every 5s)
         ↓
User clicks "Run All"
         ↓
Backend starts on localhost:8000
         ↓
User clicks "START SPARK SESSION"
         ↓
Spark initializes (30-60 seconds)
         ↓
Spark Web UI available at localhost:4040
         ↓
User clicks "LAUNCH APP"
         ↓
Main application loads
         ↓
User makes predictions and views analytics
```

---

## 📞 SUPPORT

1. **Check Status Indicators** - They show what's running
2. **Read Error Messages** - They explain what's wrong
3. **Open Browser Console** - Press F12 for detailed logs
4. **Check Terminal** - Backend logs shown there
5. **Restart Everything** - Stop and start again if needed

---

## ⏱️ EXPECTED TIMES

| Task | Time |
|------|------|
| **Backend Startup** | 5-10 seconds |
| **Spark Initialization** | 30-60 seconds |
| **Spark Sample Job** | 5-15 seconds |
| **Launcher Auto-refresh** | Every 5-10 seconds |

---

## 🎯 SUCCESS CHECKLIST

- [ ] Java installed (`java -version` works)
- [ ] PySpark installed (`pip list` shows pyspark)
- [ ] Backend started (launcher shows ✅)
- [ ] Spark initialized (green status indicator)
- [ ] Spark Web UI accessible (http://localhost:4040)
- [ ] Main app opens (http://localhost:8000 for API)

**If all checked, you're ready to use the system!** 🚀

---

**Version:** 2.0 - Neon Edition ⚡
**Last Updated:** 2024
**Status:** Production Ready ✅
