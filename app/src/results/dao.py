from app.src.models import Result

from app.src.dao.base import BaseDAO


class ResultDAO(BaseDAO):
    model = Result

    @classmethod
    async def find_by_user_id(cls, user_id: int):
        return await cls.find_all(student_id=user_id)

    @classmethod
    async def find_by_user_and_test_id(cls, user_id: int, test_id: int):
        return await cls.find_one_or_none(student_id=user_id, test_id=test_id)
