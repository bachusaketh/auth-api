# 🔐 Auth API with JWT & Role-Based Access
🚀 A production-style authentication API built with FastAPI featuring JWT authentication and role-based access control.

A backend project where I implemented a complete authentication system from scratch using FastAPI and PostgreSQL. The goal was to understand how real-world APIs handle login, security, and access control.

---

## 🚀 Features

* User registration with hashed passwords
* Login with JWT authentication
* Protected routes (only accessible with valid token)
* Role-based access control (Admin vs User)
* PostgreSQL integration using SQLAlchemy

---

## 🛠️ Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose)
* Passlib (bcrypt)

---

## 📌 API Endpoints

| Method | Endpoint  | Description             |
| ------ | --------- | ----------------------- |
| POST   | /register | Register a new user     |
| POST   | /login    | Login and get JWT token |
| GET    | /profile  | Protected route (user)  |
| GET    | /admin    | Admin-only route        |

---

## 🔐 How Authentication Works

After login, a JWT token is generated and returned to the user.
This token must be included in the request headers:

Authorization: Bearer <your_token>

The backend verifies this token before allowing access to protected routes.

---

## ⚙️ Setup Instructions

1. Clone the repo
2. Create virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add `.env` file:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/auth_db
SECRET_KEY=your_secret_key
```

5. Run server:

```bash
uvicorn app.main:app --reload
```

---

## 💡 Key Highlights
- Designed secure authentication flow using JWT
- Implemented role-based authorization (Admin/User)
- Structured project with scalable FastAPI architecture

## 📸 API Preview
![API Screenshot](screenshot.png)


## 🧠 What I Learned

* How JWT authentication works internally
* Difference between authentication and authorization
* How to structure a scalable FastAPI project
* Handling real-world issues like password hashing and token validation

---

## 📌 Future Improvements

* Add refresh tokens
* Implement logout (token blacklist)
* Add frontend (React / Next.js)

---

## 🙌 Final Note

This project helped me understand how backend authentication works beyond just theory. It gave me confidence in building secure APIs that can be extended for real-world applications.
