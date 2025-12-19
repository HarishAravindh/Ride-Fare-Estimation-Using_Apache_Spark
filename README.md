# 🚖 Ride Fare Estimation - Full-Stack Web Application

A full-stack web application for predicting ride fares using Python FastAPI backend and HTML/JavaScript frontend.

## 📋 Project Structure

```
SPARK_PROJECT/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── model.py             # Fare prediction logic
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # Web interface
└── README.md                # Setup instructions
```

## 🛠️ Tech Stack

- **Backend**: Python with FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **API**: RESTful API with CORS enabled
- **Server**: Uvicorn (ASGI server)

## 🚀 Quick Start (Easiest Way)

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser

### ⚡ One-Click Start

Simply double-click **`start_project.bat`** in the project root folder!

This will:
- Install/update all dependencies automatically
- Start the backend server
- Open the frontend in your browser

That's it! The application is ready to use.

---

## 📋 Available Batch Files

### 1. **start_project.bat** (Recommended)
Starts both backend and frontend together.
```
Double-click to run or:
start_project.bat
```

### 2. **start_backend.bat**
Starts only the backend server.
```
start_backend.bat
```

### 3. **start_frontend.bat**
Opens only the frontend (requires backend to be running).
```
start_frontend.bat
```

### 4. **stop_backend.bat**
Stops the backend server if it's running.
```
stop_backend.bat
```

---

## 🛠️ Manual Setup (Alternative)

### Step 1: Install Backend Dependencies

1. Open a terminal in VS Code (Ctrl + `)
2. Navigate to the backend folder:
   ```powershell
   cd backend
   ```

3. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```

### Step 2: Start the Backend Server

From the `backend` folder, run:

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The server will start at: `http://localhost:8000`

You should see output like:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Step 3: Open the Frontend

1. Navigate to the `frontend` folder
2. Open `index.html` in your web browser by:
   - Double-clicking the file, OR
   - Right-click → "Open with" → Choose your browser, OR
   - In VS Code, right-click `index.html` → "Open with Live Server" (if you have the Live Server extension)

## 📖 Usage Guide

### Making Predictions

The application now features **4 main tabs**:

####  1️⃣ **Prediction Tab**
1. Fill in the trip details:
   - **Distance**: Trip distance in miles (required)
   - **Duration**: Trip duration in minutes (required)
   - **Pickup Zone**: Select pickup location
   - **Dropoff Zone**: Select dropoff location
   - **Passengers**: Number of passengers (1-6)
   - **Hour of Day**: Hour in 24-hour format (0-23)
   - **Day of Week**: Select the day

2. Click **"Predict Fare (Spark)"** button - This uses Apache Spark for predictions!

3. The estimated fare will be displayed below the form

4. Click **"Open Spark Web UI"** to monitor Spark jobs in real-time

#### 2️⃣ **Analytics Tab**
- View live statistics computed using Spark SQL:
  - Average Fare
  - Average Distance
  - Average Duration
  - Total Trips
- Click "Refresh Statistics" to update data
- All computations create Spark jobs visible in the Web UI

#### 3️⃣ **History Tab**
- View your last 20 fare predictions
- See prediction timestamps, distances, durations, and fares
- Badge indicates if prediction was made using Spark
- Refresh or clear history as needed

#### 4️⃣ **About Tab**
- Learn about the technology stack
- View all features and capabilities
- Access API endpoint documentation
- Understand Spark Web UI features

### Accessing Spark Web UI

Click the **"Open Spark Web UI"** button on any tab to open Spark's monitoring interface at `http://localhost:4040`

**What you'll see in Spark UI:**
- **Jobs Tab**: All Spark jobs created by predictions and analytics
- **Stages Tab**: Detailed execution stages for each job
- **Storage Tab**: Cached data and RDDs
- **Environment Tab**: Spark configuration
- **Executors Tab**: Resource usage and metrics
- **SQL Tab**: Spark SQL query execution plans and metrics

> **Note**: The Spark Web UI will only be accessible when the backend server is running and Spark session is active.

## 🔌 API Endpoints

### GET `/`
Returns API information and available endpoints.

**Response:**
```json
{
  "message": "Ride Fare Estimation API",
  "version": "1.0",
  "endpoints": {
    "/predict": "POST - Get fare prediction",
    "/health": "GET - Health check"
  }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

### POST `/predict`
Predicts the ride fare based on trip features.

**Request Body:**
```json
{
  "distance": 5.5,
  "duration": 20,
  "pickup_zone": "Manhattan",
  "dropoff_zone": "Brooklyn",
  "passenger_count": 2,
  "hour_of_day": 17,
  "day_of_week": 4
}
```

**Response:**
```json
{
  "fare": 23.45,
  "message": "Prediction successful"
}
```

## 🧠 Model Integration

Currently, the application uses a rule-based fare calculation for demonstration. To integrate your trained ML model:

### Option 1: Using a Pickle File

1. Save your trained model:
   ```python
   import pickle
   with open('fare_model.pkl', 'wb') as f:
       pickle.dump(model, f)
   ```

2. Update `backend/model.py`:
   ```python
   # Load your model
   import pickle
   with open('fare_model.pkl', 'rb') as f:
       MODEL = pickle.load(f)
   
   def predict_fare(...):
       features = [[distance, duration, ...]]
       return MODEL.predict(features)[0]
   ```

### Option 2: Using PySpark Model

1. Add `pyspark` to `requirements.txt`
2. Load your Spark ML model in `model.py`
3. Update the prediction function accordingly

## 🎨 Customization

### Frontend Styling
Edit the `<style>` section in `frontend/index.html` to customize:
- Colors and gradients
- Button styles
- Form layout
- Animations

### Backend Logic
Modify `backend/model.py` to:
- Change fare calculation rules
- Add new features
- Integrate different ML models
- Add data preprocessing

### API Features
Extend `backend/main.py` to:
- Add new endpoints
- Implement authentication
- Add logging
- Connect to a database

## 🐛 Troubleshooting

### Backend server not starting
- Check if port 8000 is already in use
- Verify Python and pip are installed correctly
- Ensure all dependencies are installed

### CORS errors in browser
- Make sure the backend server is running
- Check that CORS is enabled in `main.py`
- Verify the API_URL in `index.html` matches your backend

### Predictions not showing
- Open browser Developer Tools (F12) → Console tab
- Check for error messages
- Verify the backend `/health` endpoint returns "healthy"

## 📝 Development Tips

1. **Auto-reload**: The FastAPI server auto-reloads on code changes (when started with `reload=True`)

2. **API Testing**: Visit `http://localhost:8000/docs` to see interactive API documentation (Swagger UI)

3. **Debugging**: Add print statements or use Python debugger in VS Code

4. **CORS**: For production, update the CORS settings to allow only your frontend domain

## 🚀 Next Steps

- [ ] Add input validation and error handling
- [ ] Integrate your trained ML model
- [ ] Add a database to store predictions
- [ ] Implement user authentication
- [ ] Deploy to cloud (Heroku, AWS, etc.)
- [ ] Add more trip features
- [ ] Create visualization dashboard
- [ ] Add historical fare tracking

## 📄 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your own ride fare estimation needs!

---

**Happy Coding! 🎉**
