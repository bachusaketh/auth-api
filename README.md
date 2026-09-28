# 🔐 Auth API — JWT Authentication & Role-Based Access Control

A backend REST API built with **FastAPI and PostgreSQL** that implements user authentication, JWT-based authorization, and role-based access control.

The project was built from scratch to understand how authentication and authorization work in a real backend application, from password hashing and JWT generation to protected routes and database integration.

## 🚀 Live Demo

**API:** https://auth-api-u9ot.onrender.com

**Swagger Documentation:** https://auth-api-u9ot.onrender.com/docs

---

## ✨ Features

- User registration with secure password hashing
- User login with JWT authentication
- Stateless authentication using JWT
- Protected routes requiring a valid access token
- Role-based access control for Users and Admins
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- Dependency-based authentication in FastAPI
- Interactive API testing with Swagger UI
- Cloud deployment using Render

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend development |
| **FastAPI** | REST API framework |
| **PostgreSQL** | Relational database |
| **SQLAlchemy** | ORM and database interaction |
| **Pydantic** | Request validation |
| **JWT / python-jose** | Authentication tokens |
| **Passlib + bcrypt** | Password hashing |
| **Uvicorn** | ASGI server |
| **Render** | API and PostgreSQL deployment |
| **Swagger / OpenAPI** | API documentation and testing |

---

## 📌 API Endpoints

| Method | Endpoint | Authentication | Description |
|---|---|---|---|
| `POST` | `/register` | Public | Register a new user |
| `POST` | `/login` | Public | Authenticate user and receive JWT |
| `GET` | `/profile` | 🔒 Required | Access authenticated user profile |
| `GET` | `/admin` | 🔒 Admin | Access admin-only resources |
| `GET` | `/` | Public | API health/status endpoint |

---

## 🔐 Authentication Flow

The authentication flow works as follows:

```text
User
 │
 ├── Register
 │      ↓
 │   Password
 │      ↓
 │   bcrypt hashing
 │      ↓
 │   PostgreSQL
 │
 └── Login
        ↓
     Verify password
        ↓
     Generate JWT
        ↓
     Access Token
        ↓
   ┌─────────────────────┐
   │ Authorization:      │
   │ Bearer <token>      │
   └─────────────────────┘
        ↓
   JWT validation
        ↓
   Check user role
        ↓
   Protected endpoint
```

After successful login, the API returns a JWT access token.

The token is sent with protected requests using:

Authorization: Bearer <your_token>

FastAPI validates the token before allowing access to protected endpoints.

---

👥 Role-Based Access Control

The API supports two roles:

User

Regular authenticated users can access:

GET /profile

Admin

Administrators can access:

GET /admin

If an authenticated user without admin privileges attempts to access /admin, the API returns:

403 Forbidden

Requests with missing, invalid, or expired authentication credentials return:

401 Unauthorized

This separates authentication (who you are) from authorization (what you're allowed to access).

🏗️ Project Structure
auth-api/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── dependencies/
│   │   └── auth.py
│   │
│   ├── core/
│   │   └── security.py
│   │
│   ├── utils/
│   │   └── token.py
│   │
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── .python-version
├── .gitignore
├── requirements.txt
├── README.md
└── screenshot.png
⚙️ Run Locally
1. Clone the repository
git clone https://github.com/bachusaketh/auth-api.git
cd auth-api
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Configure environment variables

Create a .env file in the project root:

DATABASE_URL=postgresql://postgres:yourpassword@localhost/auth_db
SECRET_KEY=your_secret_key

Never commit .env or expose database credentials and secret keys publicly.

5. Start the API
uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs
☁️ Deployment

The API is deployed using Render with a managed PostgreSQL database.

Deployment Architecture
GitHub Repository
       │
       ↓
Render Web Service
       │
       ↓
FastAPI + Uvicorn
       │
       ↓
Render PostgreSQL

Environment variables are configured through Render rather than committed to the repository.

Live API

https://auth-api-u9ot.onrender.com

Live Swagger Documentation

https://auth-api-u9ot.onrender.com/docs

🔒 Security Highlights
Passwords are never stored in plain text
Passwords are hashed using bcrypt
JWT tokens are used for stateless authentication
Protected routes validate JWT credentials before access
Role-based authorization restricts admin resources
Secrets are stored using environment variables
.env is excluded from version control
Authentication and authorization logic are separated using FastAPI dependencies
📸 API Preview

🧠 Key Implementation Concepts

This project helped me understand and implement:

JWT structure and token-based authentication
Authentication vs authorization
Password hashing with bcrypt
Stateless authentication
FastAPI dependency injection
Protected API routes
Role-based access control
PostgreSQL integration with SQLAlchemy
Pydantic request validation
HTTP 401 vs 403 responses
API testing with Swagger/OpenAPI
Environment-based configuration
Deploying a Python API and PostgreSQL database to the cloud
🔮 Future Improvements

Potential improvements for the next version:

Refresh token implementation
Token revocation / logout
Redis-based token blacklist
Rate limiting for authentication endpoints
Email verification
Password reset functionality
Automated tests with Pytest
Docker containerization
CI/CD pipeline
React frontend
👨‍💻 Author

Bachu Saketh

Computer Science Engineer | Backend & GenAI Developer

GitHub: https://github.com/bachusaketh

📄 License

This project is available for educational and portfolio purposes.

