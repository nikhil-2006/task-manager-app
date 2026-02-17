# Task Manager Application

A full-stack Task Manager web application built with:

- Frontend: React.js (Axios, Bootstrap)
- Backend: Django REST Framework
- Authentication: JWT (JSON Web Token)
- Database: SQLite (default Django DB)

---

## 🚀 Features

- User Registration
- User Login with JWT Authentication
- Protected Dashboard
- Create Task
- View Tasks
- Update Task
- Delete Task
- Search Tasks
- Responsive Sidebar Navigation
- Mobile Friendly UI

---

## 🛠 Tech Stack

### Frontend
- React.js
- Axios
- Bootstrap
- React Router

### Backend
- Django
- Django REST Framework
- Simple JWT

---

## 📂 Project Structure

```
task-manager-app/
│
├── frontend/
│   ├── src/
│   └── ...
│
├── backend/
│   ├── tasks/
│   ├── auth/
│   └── ...
│
├── log.txt
├── frontend-log.txt
└── README.md
```

---

## 🔐 Authentication Flow

1. User logs in
2. Backend returns JWT Access & Refresh tokens
3. Tokens stored in localStorage
4. Protected routes verify access token
5. Dashboard loads user data

---

## 📡 API Endpoints

### Auth

- POST `/api/auth/register/`
- POST `/api/auth/login/`
- GET `/api/auth/profile/`

### Tasks

- GET `/api/tasks/`
- POST `/api/tasks/`
- PUT `/api/tasks/{id}/`
- DELETE `/api/tasks/{id}/`

---

## 🧪 How To Run The Project

### Backend

```bash
cd backend
python manage.py runserver
```

Runs at:
```
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend
npm install
npm start
```

Runs at:
```
http://localhost:3000
```

---

## 📦 Postman Collection

API endpoints tested using Postman.
All CRUD operations verified successfully.

---

## 📈 Production Scaling Strategy

For production deployment:

- Use PostgreSQL instead of SQLite
- Store JWT in HTTP-only cookies
- Enable CORS properly
- Use Nginx for reverse proxy
- Deploy backend on AWS / Railway / Render
- Deploy frontend on Vercel / Netlify
- Enable HTTPS
- Add logging & monitoring (Sentry / LogRocket)

---

## 👨‍💻 Author

Nikhil  
B.Tech IT Student  
Frontend Developer Intern Candidate  

---

## ✅ Status

✔ Authentication Working  
✔ CRUD Operations Working  
✔ Protected Routes Working  
✔ Responsive UI  
✔ Full Stack Integration Complete  

