from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin
from app.core.security import hash_password
from app.core.security import verify_password
from app.utils.token import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    print("Incoming password:", user.password, type(user.password))  # debug

    hashed_pw = hash_password(user.password)

    new_user = User(
        email=user.email,
        password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "Invalid email or password"}

    if not verify_password(user.password, db_user.password):
        return {"error": "Invalid email or password"}

    token = create_access_token({
        "sub": db_user.id,
        "role": db_user.role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

from app.dependencies.auth import get_current_user

@router.get("/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": current_user
    }

from app.dependencies.auth import require_admin

@router.get("/admin")
def admin_route(current_user: dict = Depends(require_admin)):
    return {
        "message": "Welcome Admin",
        "user": current_user
    }