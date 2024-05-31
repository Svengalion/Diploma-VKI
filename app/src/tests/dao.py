from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.src.database import async_session_maker
from app.src.models import Test, Question, Answer, AnswerToQuestion
from app.src.dao.base import BaseDAO


class TestDAO(BaseDAO):
    model = Test

    @classmethod
    async def find_with_details(cls, test_id: int):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .options(
                    selectinload(Test.answer_to_question).selectinload(AnswerToQuestion.question).selectinload(
                        Question.answer_to_question).selectinload(AnswerToQuestion.answer)
                )
                .filter(cls.model.id == test_id)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()


class AnswerToQuestionDAO(BaseDAO):
    model = AnswerToQuestion