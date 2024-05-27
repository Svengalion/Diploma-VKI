from fastapi import APIRouter, Depends, Response, UploadFile, File

from app.src.users.dependencies import (
    current_user,
    register_user,
    login_user,
    update_username,
    upload_avatar, get_image
)
from app.src.models import User
from app.src.users.schemas import SUserAuth, SUpdateUsername, SUser

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/registration")
async def register(user_data: SUserAuth):
    await register_user(user_data)


@router.post("/login")
async def login(response: Response, user_data: SUserAuth):
    return await login_user(user_data, response)


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("booking_access_token")


@router.get("/me", response_model=SUser)
async def me(current_user: User = Depends(current_user)):
    return current_user


@router.put("/update-name", response_model=SUser)
async def update_username(update_data: SUpdateUsername, user: User = Depends(current_user)):
    return await update_username(update_data, user)


@router.put("/upload-avatar")
async def upload_image(file: UploadFile = File(...), user: User = Depends(current_user)):
    return await upload_avatar(file, user)


@router.get("/avatar")
async def get_avatar(user: User = Depends(current_user)):
    return await get_image(user)
