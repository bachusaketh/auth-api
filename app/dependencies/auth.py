from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.config import SECRET_KEY

security = HTTPBearer()

ALGORITHM = "HS256"

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        role = payload.get("role")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"user_id": user_id, "role": role}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
from app.dependencies.auth import get_current_user
def require_admin(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")

    return current_user