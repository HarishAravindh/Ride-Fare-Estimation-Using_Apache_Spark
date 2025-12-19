# 🚖 SPARK PROJECT - Authentication System Quick Start

## 🎯 Complete Flow Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│                   index.html                                     │
│            (ACCESS SYSTEM - Entry Point)                        │
│                                                                   │
│   🚖 RIDE FARE ESTIMATION                                       │
│   ⚡ KARUR CITY - NEON-POWERED SYSTEM ⚡                        │
│                                                                   │
│   [⚡ ACCESS SYSTEM ⚡] (Parallelogram Button)                  │
│                                                                   │
│   🚀 SYSTEM ACCESS                                              │
│   • Secure system for Karur City ride fare estimation          │
│   • Click the button above to access the prediction system     │
│   • All data is processed locally and securely.                │
└─────────────────────────────────────────────────────────────────┘
                            ↓
                     Redirects to login.html


┌────────────────────────────────────────────────────────────────────┐
│                   login.html                                        │
│              (USER LOGIN - Authentication)                         │
│                                                                      │
│   🚖 USER LOGIN                                                    │
│   ⚡ KARUR CITY - NEON-POWERED SYSTEM ⚡                          │
│                                                                      │
│   [Form Box - Parallelogram]                                       │
│   ┌──────────────────────────────────────────┐                   │
│   │  👤 USER ID:                             │                   │
│   │  [____________________]                  │                   │
│   │                                          │                   │
│   │  🔐 PASSWORD:                            │                   │
│   │  [____________________]                  │                   │
│   │                                          │                   │
│   │  [⚡ LOGIN ⚡]                           │                   │
│   │  ──────────────────                     │                   │
│   │  [📝 NEW USER? REGISTER]  [🔑 CHANGE PASSWORD]              │
│   └──────────────────────────────────────────┘                   │
│                                                                      │
│   Default Credentials:                                             │
│   • admin / admin123                                               │
│   • user1 / password1                                              │
│   • testuser / test123                                             │
└────────────────────────────────────────────────────────────────────┘
         ↙                              ↓                    ↘
    Registers              Logs In      (Valid Creds)    Change Password
        ↓                    ↓              ↓                    ↓
   register.html       index_main.html  SUCCESS!          change_password.html


┌────────────────────────────────────────────────────────────────────┐
│                 register.html                                       │
│          (NEW USER REGISTRATION)                                   │
│                                                                      │
│   🚖 NEW USER REGISTRATION                                         │
│   ⚡ KARUR CITY - NEON-POWERED SYSTEM ⚡                          │
│                                                                      │
│   [Form Box - Parallelogram]                                       │
│   ┌──────────────────────────────────────────┐                   │
│   │  👤 USER ID:                             │                   │
│   │  [____________________]                  │                   │
│   │  • Min 3 characters, must be unique     │                   │
│   │                                          │                   │
│   │  🔐 PASSWORD:                            │                   │
│   │  [____________________]                  │                   │
│   │  • Min 6 characters                     │                   │
│   │                                          │                   │
│   │  ✓ CONFIRM PASSWORD:                    │                   │
│   │  [____________________]                  │                   │
│   │  • Must match password above            │                   │
│   │                                          │                   │
│   │  [📝 CREATE ACCOUNT 📝]                 │                   │
│   │  ──────────────────────                │                   │
│   │  [🔐 BACK TO LOGIN]                    │                   │
│   └──────────────────────────────────────────┘                   │
│                                                                      │
│   Features:                                                         │
│   ✅ Unique user ID validation                                    │
│   ✅ Password requirements display                                │
│   ✅ Confirmation matching                                        │
│   ✅ Success notification                                         │
│   ✅ Auto-redirect to login                                       │
└────────────────────────────────────────────────────────────────────┘
                            ↓
                   Redirects to login.html


┌────────────────────────────────────────────────────────────────────┐
│             change_password.html                                    │
│        (PASSWORD MANAGEMENT - For Logged-In Users)                 │
│                                                                      │
│   🚖 CHANGE PASSWORD                                               │
│   ⚡ KARUR CITY - NEON-POWERED SYSTEM ⚡                          │
│                                                                      │
│   ✅ Logged in as: User One (user1)                               │
│                                                                      │
│   [Form Box - Parallelogram]                                       │
│   ┌──────────────────────────────────────────┐                   │
│   │  👤 USER ID:                             │                   │
│   │  [user1_______________] (Read-Only)      │                   │
│   │                                          │                   │
│   │  🔐 CURRENT PASSWORD:                    │                   │
│   │  [____________________]                  │                   │
│   │  • Your current password                │                   │
│   │                                          │                   │
│   │  ✨ NEW PASSWORD:                        │                   │
│   │  [____________________]                  │                   │
│   │  • Min 6 characters                     │                   │
│   │                                          │                   │
│   │  ✓ CONFIRM NEW PASSWORD:                │                   │
│   │  [____________________]                  │                   │
│   │  • Must match new password              │                   │
│   │                                          │                   │
│   │  [🔑 CHANGE PASSWORD 🔑]                │                   │
│   │  ──────────────────────                │                   │
│   │  [🔐 BACK TO LOGIN]                    │                   │
│   └──────────────────────────────────────────┘                   │
│                                                                      │
│   Features:                                                         │
│   ✅ Current password verification                                │
│   ✅ New password validation                                      │
│   ✅ Password change confirmation                                 │
│   ✅ Auto-logout after change                                     │
│   ✅ Auto-redirect to login                                       │
└────────────────────────────────────────────────────────────────────┘
                            ↓
                    Auto-Logout & Redirect
                            ↓
                   Redirects to login.html


┌────────────────────────────────────────────────────────────────────┐
│                 index_main.html                                     │
│           (MAIN APPLICATION - After Login)                         │
│                                                                      │
│   🚖 LEFT SIDEBAR                     MAIN CONTENT                │
│   ┌──────────────────┐   ┌──────────────────────────────┐         │
│   │ 🚖 RIDE FARE    │   │ 🤖 RIDE FARE ESTIMATION 🚖 │         │
│   │                  │   │ ⚡ KARUR CITY - NEON-POW...│         │
│   │ ⚡ PREDICT FARE │   │                              │         │
│   │ 📊 STATISTICS  │   │ [⚡ START RUN SERVER ⚡]   │         │
│   │ 📜 HISTORY     │   │                              │         │
│   │ 🔥 SPARK UI    │   │ ┌─────────────────────────┐ │         │
│   │ ℹ️  ABOUT      │   │ │ PREDICT TAB CONTENT:    │ │         │
│   │ ⚡ RUN SERVER  │   │ │ • Distance input       │ │         │
│   │ 🚪 LOGOUT      │   │ │ • Duration input       │ │         │
│   │                  │   │ │ • Pickup/Dropoff zones│ │         │
│   └──────────────────┘   │ │ • Passenger count      │ │         │
│                          │ │ • Time inputs          │ │         │
│                          │ │ • COMPUTE FARE button  │ │         │
│                          │ │ • Result display       │ │         │
│                          │ └─────────────────────────┘ │         │
│                          │                              │         │
│                          │ STATS TAB:                   │         │
│                          │ • Average Fare              │         │
│                          │ • Average Distance          │         │
│                          │ • Average Time              │         │
│                          │ • Total Trips               │         │
│                          │ • REFRESH DATA button       │         │
│                          │                              │         │
│                          │ OTHER TABS:                 │         │
│                          │ • History (Prediction Log)  │         │
│                          │ • Spark UI (Job Monitor)    │         │
│                          │ • About (System Info)       │         │
│                          └──────────────────────────────┘         │
│                                                                      │
│   Features:                                                         │
│   ✅ Login state verification                                     │
│   ✅ Sidebar navigation                                           │
│   ✅ Multiple tabs (Predict, Stats, History, Spark, About)      │
│   ✅ Real-time fare estimation                                    │
│   ✅ Statistics and analytics                                     │
│   ✅ Prediction history tracking                                  │
│   ✅ Spark UI integration                                         │
│   ✅ Logout functionality                                         │
└────────────────────────────────────────────────────────────────────┘
```

---

## 🔐 User Credentials (Default Test Users)

| User ID | Password | Name |
|---------|----------|------|
| `admin` | `admin123` | Admin User |
| `user1` | `password1` | User One |
| `testuser` | `test123` | Test User |

---

## 📋 Testing Checklist

### ✅ ACCESS SYSTEM Page
- [ ] Open index.html
- [ ] See parallelogram button with neon effects
- [ ] Click button
- [ ] Redirects to login.html

### ✅ LOGIN Page
- [ ] Form displays correctly
- [ ] Test invalid credentials → Error message
- [ ] Test with admin/admin123 → Success
- [ ] Click "NEW USER? REGISTER" → Goes to register.html
- [ ] Click "CHANGE PASSWORD" → Goes to change_password.html

### ✅ REGISTER Page
- [ ] Form displays correctly
- [ ] Try existing user ID → Error message
- [ ] Try short password → Error message
- [ ] Try non-matching passwords → Error message
- [ ] Register new user (e.g., "newuser" / "newpass123")
- [ ] Success message appears
- [ ] Auto-redirects to login.html
- [ ] Login with new credentials → Works!

### ✅ CHANGE PASSWORD Page
- [ ] When not logged in → "Not logged in" message
- [ ] Login first, then access change password
- [ ] Enter wrong current password → Error
- [ ] Enter non-matching new passwords → Error
- [ ] Change password successfully
- [ ] Auto-logout and redirect to login
- [ ] Login with new password → Works!

### ✅ MAIN APP Page
- [ ] After successful login → Lands on index_main.html
- [ ] Sidebar visible with menu items
- [ ] All tabs work (Predict, Stats, History, Spark, About)
- [ ] Logout button works
- [ ] After logout → Redirects to login.html

---

## 💾 Data Storage (localStorage)

```javascript
// User Database
localStorage.registeredUsers = {
  "admin": { password: "admin123", name: "Admin User" },
  "user1": { password: "password1", name: "User One" },
  "testuser": { password: "test123", name: "Test User" },
  // ... custom registered users
}

// Session State
localStorage.isLoggedIn = "true"
localStorage.userId = "admin"
localStorage.username = "Admin User"
```

---

## 🎨 Design Features

- **Theme**: Dark Cyberpunk (Black, Cyan, Magenta)
- **Shapes**: Parallelogram clip-paths on buttons and forms
- **Colors**:
  - Primary: Cyan (#0ff)
  - Accent: Magenta (#f0f)
  - Success: Green (#0f0)
  - Error: Red (#f00)
- **Effects**: 
  - Neon glows
  - Pulsing animations
  - Scanline effects
  - Matrix background
  - Hover transforms
- **Responsiveness**: Mobile-friendly design

---

## 🚀 Ready to Use!

All authentication pages are fully functional and integrated. Users can:
1. ✅ Access the system
2. ✅ Login with credentials
3. ✅ Register new accounts
4. ✅ Change passwords
5. ✅ Access main application
6. ✅ Logout safely

**Enjoy your SPARK PROJECT authentication system!** 🎉

Created: December 13, 2025
