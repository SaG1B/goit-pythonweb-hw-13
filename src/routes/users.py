from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas import UserResponse
from src.services.auth import auth_service
from src.services.upload_image import UploadImage

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: User = Depends(auth_service.get_current_user)):
    return current_user

@router.patch("/avatar", response_model=UserResponse)
async def update_avatar_user(
    file: UploadFile = File(...),
    current_user: User = Depends(auth_service.get_current_user),
    db: Session = Depends(get_db)
):
    public_id = f"UsersApp/{current_user.username}_{current_user.id}"
    res = UploadImage.upload_image(file.file, public_id)
    src_url = res.get("secure_url")
    
    current_user.avatar = src_url
    db.commit()
    db.refresh(current_user)
    return current_user
