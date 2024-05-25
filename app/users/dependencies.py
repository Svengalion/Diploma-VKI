from datetime import datetime

from fastapi import Request, Depends
from jose import jwt, JWTError

from app.config import settings
from app.exceptions import TokenExpired, TokenAbsent, IncorrectToken, IncorrectUser
from app.users.dao import UserDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
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
