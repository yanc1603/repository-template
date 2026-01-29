from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext
from app.core.database import get_db
from .models import User
from .schemas import UserCreate, UserLogin, UserResponse
from fastapi.responses import JSONResponse

router = APIRouter(tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check existing
    result = await db.execute(select(User).where(User.username == user_data.username))
    if result.scalars().first():
         raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, password_hash=hashed)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/login")
async def login(user_data: UserLogin, request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user_data.username))
    user = result.scalars().first()
    
    if user and verify_password(user_data.password, user.password_hash):
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        return {"success": True, "message": "Logged in successfully", "user": {"id": user.id, "username": user.username}}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.get("/me")
async def get_current_user(request: Request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    if user_id:
        return {"authenticated": True, "user": {"id": user_id, "username": username}}
    return {"authenticated": False}

@router.post("/logout")
async def logout(request: Request):
    request.session.clear()
    return {"success": True, "message": "Logged out"}
