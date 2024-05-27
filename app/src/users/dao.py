from app.src.models import User

from app.src.dao.base import BaseDAO
from app.src.database import async_session_maker


class UserDAO(BaseDAO):
    model = User
    @classmethod
    async def get_image_path(cls, user_id: int):
        async with async_session_maker() as session:
            user = await cls.find_by_id(user_id)
            return user.image_path if user else None