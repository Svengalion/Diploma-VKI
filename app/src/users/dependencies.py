import os
from datetime import datetime

from fastapi import Depends, Response, Request, UploadFile
from jose import jwt, JWTError
from starlette.responses import FileResponse

from app.src.config import settings
from app.src.exceptions import TokenExpired, TokenAbsent, IncorrectToken, IncorrectUser, UserAlreadyExists, \
    IncorrectLogin, AvatarNotFound
from app.src.users.dao import UserDAO
from app.src.users.auth import get_password_hash, authenticate_user, create_access_token
from app.src.users.schemas import SUserAuth, SUpdateUsername
from app.src.models import User


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsent
    return token


async def current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.KEY, settings.ALGORITHM)
    except JWTError:
        raise IncorrectToken
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpired
    user_id: str = payload.get("sub")
    if not user_id:
        raise IncorrectUser
    user = await UserDAO.find_by_id(int(user_id))
    if not user:
        raise IncorrectUser
    return user


async def register_user(user_data: SUserAuth):
    existing_user = await UserDAO.find_one_or_none(login=user_data.login)
    if existing_user:
        raise UserAlreadyExists
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.insert_data(login=user_data.login, password=hashed_password)


async def login_user(user_data: SUserAuth, response: Response):
    user = await authenticate_user(user_data.login, user_data.password)
    if not user:
        raise IncorrectLogin
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return access_token


async def update_name(update_data: SUpdateUsername, user: User):
    await UserDAO.update(user.id, name=update_data.name)
    user.name = update_data.name
    return user


async def upload_avatar(file: UploadFile, user: User):
    file_location = f"app/materials/photos/{user.id}_{file.filename}"
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    if user.image_path:
        old_file_location = user.image_path
        if os.path.exists(old_file_location):
            os.remove(old_file_location)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    await UserDAO.update(user.id, image_path=file_location)
    return {"info": "File uploaded successfully", "file_location": file_location}


async def get_image(user: User):
    image_path = await UserDAO.get_image_path(user.id)
    if not image_path or not os.path.exists(image_path):
        raise AvatarNotFound
    return FileResponse(image_path)
