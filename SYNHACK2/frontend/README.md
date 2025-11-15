# VNIT Hostel Grievance Management System - Frontend

React-based frontend for the VNIT Hostel Grievance Management System.

## Setup

1. **Install dependencies:**
```bash
cd frontend
npm install
```

2. **Start the development server:**
```bash
npm start
```

The app will open at http://localhost:3000

## Features

### Student Portal
- Register and login
- File new complaints
- View complaint history
- Track complaint status in real-time
- Emergency detection

### Admin Dashboard
- View all complaints with filters
- Role-based views (validator, supervisor, warden, dean)
- Dashboard statistics
- Validate and assign complaints

### Worker Dashboard
- View assigned tasks
- Update task status
- Mark tasks as completed
- View deadlines

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── pages/
│   │   ├── Login.js
│   │   ├── Register.js
│   │   ├── StudentDashboard.js
│   │   ├── AdminDashboard.js
│   │   └── WorkerDashboard.js
│   ├── api.js          # API integration
│   ├── App.js          # Main app component
│   ├── App.css         # Styles
│   └── index.js        # Entry point
└── package.json
```

## API Integration

The frontend connects to the Flask backend at `http://localhost:5001/api`

Make sure your Flask backend is running before starting the frontend.

## Building for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## Test Credentials

After setting up admin roles in the backend:

- **Student:** STUDENT002 / password123
- **Validator:** VALIDATOR001 / password123
- **Supervisor:** SUPERVISOR001 / password123
- **Worker:** WORKER001 / password123
