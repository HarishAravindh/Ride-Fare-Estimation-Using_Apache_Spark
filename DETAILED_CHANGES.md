# 📝 DETAILED CODE CHANGES - All Fixes

## 1. Select Element Styling Fix
**File:** `frontend/index.html` (Lines 306-340)
**Change:** Updated CSS for pickup_zone, dropoff_zone, day_of_week

```css
/* BEFORE */
#pickup_zone, #dropoff_zone, #day_of_week {
    color: #0ff !important;
    background: rgba(0, 0, 0, 0.5) !important;
    border: 2px solid #0ff !important;
    padding: 8px;
}

#pickup_zone:focus, #dropoff_zone:focus, #day_of_week:focus {
    color: #0ff !important;
    background: rgba(0, 255, 255, 0.1) !important;
    border: 2px solid #0ff !important;
}

/* AFTER */
#pickup_zone, #dropoff_zone, #day_of_week {
    color: #0ff !important;
    background: #000 !important;           /* Pure black, not transparent */
    border: 2px solid #0ff !important;
    padding: 8px;
}

#pickup_zone:focus, #dropoff_zone:focus, #day_of_week:focus {
    color: #000 !important;                /* Black text on magenta */
    background: #f0f !important;           /* Magenta/Pink background */
    border: 2px solid #f0f !important;
    box-shadow: 0 0 20px #f0f !important;  /* Neon glow */
    outline: none;
}
```

---

## 2. Add Visible RUN Button
**File:** `frontend/index.html` (Lines 600-615)
**Change:** Added prominent button after page header

```html
<!-- ADDED after cyber-header -->
<div style="text-align: center; margin: 20px 0;">
    <a href="launcher.html" target="_blank" class="cyber-btn" 
       style="display: inline-block; padding: 15px 40px; font-size: 1.2em; 
              background: linear-gradient(45deg, #0ff, #f0f); color: #000; 
              text-decoration: none; border-radius: 8px; 
              box-shadow: 0 0 30px #0ff, 0 0 60px #f0f; transition: all 0.3s; cursor: pointer;">
        ⚡ START RUN SERVER ⚡
    </a>
</div>
```

---

## 3. Remove Visualization Section from Predict Tab
**File:** `frontend/index.html` (Lines 693-710 REMOVED)
**Change:** Deleted visualization buttons and container

```html
<!-- REMOVED -->
<div id="vizSection" style="...">
    <button id="showBreakdownBtn" class="cyber-btn" onclick="showBreakdown()">
        📊 SHOW FARE BREAKDOWN
    </button>
    <div id="breakdownWrap" style="...">
        <canvas id="breakdownChart"></canvas>
    </div>
</div>
```

---

## 4. Add Visualization Section to Statistics Tab
**File:** `frontend/index.html` (Lines 738-745 ADDED)
**Change:** Added breakdown chart to stats tab

```html
<!-- ADDED to id="stats" tab -->
<div style="margin-top: 40px; border-top: 2px solid #0ff; padding-top: 20px;">
    <div style="color:#0ff; margin-bottom:15px; font-size:1.1em; text-align: center;">
        📈 FARE BREAKDOWN ANALYSIS
    </div>
    <canvas id="breakdownChart" width="800" height="300" 
            style="background:#000; border:1px solid #0ff; margin-top: 15px;"></canvas>
</div>
```

---

## 5. Remove Right Sidebar Visualization
**File:** `frontend/index.html` (Lines 806-813 REMOVED)
**Change:** Deleted entire `<aside>` element

```html
<!-- REMOVED -->
<aside class="sidebar-right">
    <h3>📊 FARE BREAKDOWN</h3>
    <canvas id="breakdownChart" width="350" height="300"></canvas>
</aside>
```

---

## 6. Remove renderSidebarBreakdown Function
**File:** `frontend/index.html` (Lines 990-1043 REMOVED)
**Change:** Deleted old sidebar rendering function

```javascript
/* REMOVED */
async function renderSidebarBreakdown(formData) {
    // ... entire function deleted (54 lines)
}
```

---

## 7. Update loadStats Function
**File:** `frontend/index.html` (Lines 884-896)
**Change:** Added call to showBreakdown()

```javascript
/* BEFORE */
async function loadStats() {
    try {
        const response = await fetch(`${API_URL}/stats`);
        const stats = await response.json();
        
        document.getElementById('avgFare').textContent = `₹${stats.avg_fare.toFixed(2)}`;
        document.getElementById('avgDistance').textContent = `${stats.avg_distance.toFixed(1)} km`;
        document.getElementById('avgDuration').textContent = `${stats.avg_duration.toFixed(0)} min`;
        document.getElementById('totalTrips').textContent = stats.total_trips;
    } catch (error) {
        console.error('Stats error:', error);
    }
}

/* AFTER */
async function loadStats() {
    try {
        const response = await fetch(`${API_URL}/stats`);
        const stats = await response.json();
        
        document.getElementById('avgFare').textContent = `₹${stats.avg_fare.toFixed(2)}`;
        document.getElementById('avgDistance').textContent = `${stats.avg_distance.toFixed(1)} km`;
        document.getElementById('avgDuration').textContent = `${stats.avg_duration.toFixed(0)} min`;
        document.getElementById('totalTrips').textContent = stats.total_trips;

        // Load the breakdown chart with default values
        await showBreakdown();
    } catch (error) {
        console.error('Stats error:', error);
    }
}
```

---

## 8. Simplify showBreakdown Function
**File:** `frontend/index.html` (Lines 930-975)
**Change:** Removed wrap element reference, added default values

```javascript
/* BEFORE */
async function showBreakdown() {
    const wrap = document.getElementById('breakdownWrap');  // ❌ No longer exists
    try {
        // ... code tries to set wrap.style.display
        // ... uses old colors
    }
}

/* AFTER */
async function showBreakdown() {
    try {
        const formData = {
            distance: parseFloat(document.getElementById('distance').value) || 5.0,
            duration: parseFloat(document.getElementById('duration').value) || 20,
            pickup_zone: document.getElementById('pickup_zone').value || 'Central',
            dropoff_zone: document.getElementById('dropoff_zone').value || 'Central',
            passenger_count: parseInt(document.getElementById('passenger_count').value) || 1,
            hour_of_day: parseInt(document.getElementById('hour_of_day').value) || 12,
            day_of_week: parseInt(document.getElementById('day_of_week').value) || 1
        };

        const resp = await fetch(`${API_URL}/breakdown`, { 
            method: 'POST', 
            headers: {'Content-Type':'application/json'}, 
            body: JSON.stringify(formData) 
        });
        if(!resp.ok) throw new Error('Breakdown request failed');
        const data = await resp.json();
        const comps = data.components;

        const labels = ['Base','Distance','Time','Passenger Fee','Surge Impact','Weekend Impact','Taxes/Fees'];
        const values = [comps.base_fare, comps.distance_fare, comps.time_fare, comps.passenger_fee, comps.surge_impact, comps.weekend_impact, comps.taxes_fees];

        const ctx = document.getElementById('breakdownChart');
        if (!ctx) return;  // Chart not available
        
        const ctxObj = ctx.getContext('2d');
        if(breakdownChart) breakdownChart.destroy();
        breakdownChart = new Chart(ctxObj, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Fare Components (₹)',
                    data: values,
                    backgroundColor: ['#667eea','#764ba2','#f093fb','#f6d365','#ff7e5f','#7db9b6','#b0c4de'],
                    borderColor: '#0ff',
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                plugins: { legend: { display: false } },
                scales: { x: { ticks: { color: '#0ff' } }, y: { ticks: { color: '#0ff' } } }
            }
        });

    } catch (err) {
        console.warn('Breakdown chart error:', err.message);
    }
}
```

---

## 9. Remove renderSidebarBreakdown Call from Load Event
**File:** `frontend/index.html` (Page load event)
**Change:** Removed initialization of sidebar visualization

```javascript
/* BEFORE */
window.addEventListener('load', async () => {
    // ... other code
    loadStats();
    
    // Initialize sidebar breakdown with default values  ❌ REMOVED
    const defaultFormData = { distance: 5.0, ... };
    renderSidebarBreakdown(defaultFormData);
    
    // ... rest of code
});

/* AFTER */
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if(response.ok) {
            console.log('✅ Backend connected');
            loadStats();

            const s = await getSparkStatus();
            const ui = s && s.ui_url ? s.ui_url : 'http://localhost:4040';
            const tabSpan = document.getElementById('sparkTabUrl');
            if (tabSpan) tabSpan.textContent = ui;
        }
    } catch {
        console.warn('⚠️ Backend offline');
    }
});
```

---

## 10. Enhanced Spark Error Handling
**File:** `backend/main.py` (Lines 71-90)
**Change:** Better error messages for debugging

```python
/* BEFORE */
@app.post("/start-spark")
def start_spark():
    try:
        spark = get_spark_session()
        try:
            stats = create_sample_data()
        except Exception:
            stats = None
        # ... return
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to start Spark: {e}")

/* AFTER */
@app.post("/start-spark")
def start_spark():
    try:
        spark = get_spark_session()
        try:
            stats = create_sample_data()
        except Exception as e:
            print(f"⚠️ Sample data creation failed: {e}")
            stats = None
        # ... return
    except Exception as e:
        error_detail = f"Failed to start Spark: {str(e)}\nEnsure:\n1. Java is installed\n2. PySpark is installed (pip install pyspark)\n3. JAVA_HOME environment variable is set"
        print(f"❌ Spark initialization error: {error_detail}")
        raise HTTPException(status_code=500, detail=error_detail)
```

---

## 11. Add RUN Button to Hamburger Version
**File:** `frontend/index_hamburger.html` (Lines 679-688)
**Change:** Same prominent button added after header

```html
<!-- ADDED to hamburger version -->
<div style="text-align: center; margin: 20px 0;">
    <a href="launcher.html" target="_blank" class="cyber-btn" 
       style="display: inline-block; padding: 15px 40px; font-size: 1.2em; 
              background: linear-gradient(45deg, #0ff, #f0f); color: #000; 
              text-decoration: none; border-radius: 8px; 
              box-shadow: 0 0 30px #0ff, 0 0 60px #f0f; transition: all 0.3s; cursor: pointer;">
        ⚡ START RUN SERVER ⚡
    </a>
</div>
```

---

## Summary of Line Changes

| File | Changes | Lines |
|------|---------|-------|
| index.html | Select styling | 306-340 |
| index.html | Add RUN button | 600-615 |
| index.html | Remove viz from predict | 693-710 |
| index.html | Add viz to stats | 738-745 |
| index.html | Remove right sidebar | 806-813 |
| index.html | Remove renderSidebarBreakdown function | 990-1043 |
| index.html | Update loadStats | 884-896 |
| index.html | Simplify showBreakdown | 930-975 |
| index.html | Update window load event | ~1085-1105 |
| index_hamburger.html | Add RUN button | 679-688 |
| main.py | Enhanced error handling | 71-90 |

**Total: ~200+ lines of code changes/removals/additions across 3 files**
