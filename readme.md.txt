# 🚀 Task Manager Web Application

A full-stack web application built using **React (Frontend)** and **Django REST Framework (Backend)** with secure JWT authentication.

This project demonstrates authentication, protected routes, CRUD operations, responsive UI design, and scalability considerations.

---

## 📌 Features

### 🔐 Authentication
- User Registration
- JWT-based Login
- Protected Dashboard Routes
- Secure Logout
- Password hashing (Django default secure hashing)

### 📊 Dashboard
- Display logged-in user profile
- Create Tasks
- Update Tasks
- Delete Tasks
- Search Tasks
- Responsive Sidebar Navigation

### 🛡 Security
- JWT authentication middleware
- Protected API endpoints
- Server-side validation
- Unauthorized access handling (401)

---

## 🏗 Tech Stack

### Frontend
- React (Create React App)
- Axios
- Bootstrap 5
- Responsive design

### Backend
- Django
- Django REST Framework
- SimpleJWT
- SQLite (Can scale to PostgreSQL)

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Backend runs at:

http://127.0.0.1:8000/


Frontend Setup:

cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000/


🔑 API Endpoints

Authentication

Method	Endpoint		Description

POST	/api/auth/register/	Register user
POST	/api/auth/login/	Login user
GET	/api/auth/profile/	Get profile

Tasks:

Method	Endpoint		Description

GET	/api/tasks/		List tasks
POST	/api/tasks/		Create task
PUT	/api/tasks/{id}/	Update task
DELETE	/api/tasks/{id}/	Delete task

