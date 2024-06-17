from sqlalchemy.future import select
from sqlalchemy.orm import selectinload, joinedload
from app.src.database import async_session_maker
from app.src.models import Test, Question, Answer, AnswerToQuestion
from app.src.dao.base import BaseDAO
from app.src.tests.schemas import SQuestion, SAnswer


class TestDAO(BaseDAO):
    model = Test

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .filter_by(**filter_by)
                .order_by(cls.model.id)
            )
            result = await session.execute(query)
            tests = result.scalars().unique().all()
            return tests

    @classmethod
    async def find_with_details(cls, test_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(
                    selectinload(Test.answer_to_question).selectinload(AnswerToQuestion.question),
                    selectinload(Test.answer_to_question).selectinload(AnswerToQuestion.answer)
                )
                .filter(cls.model.id == test_id)
            )
            result = await session.execute(query)
            test = result.scalar_one_or_none()
            return test


class AnswerToQuestionDAO(BaseDAO):
    model = AnswerToQuestion
