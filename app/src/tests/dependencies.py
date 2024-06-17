from fastapi import Depends, HTTPException
from sqlalchemy import select
from app.src.tests.dao import TestDAO, AnswerToQuestionDAO
from app.src.tests.schemas import STest, SAnswer, SQuestion, STestQuests
from app.src.models import Test
from app.src.database import async_session_maker
from app.src.exceptions import AnswerNotFound


async def current_test(test_id: int):
    test = await TestDAO.find_with_details(test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")

    questions_dict = {}
    for atq in test.answer_to_question:
        question = atq.question
        if question.id not in questions_dict:
            questions_dict[question.id] = {
                'id': question.id,
                'question': question.question,
                'answers': []
            }
        questions_dict[question.id]['answers'].append(SAnswer.from_orm(atq.answer))

    questions = [SQuestion(**q) for q in questions_dict.values()]
    return STestQuests(questions=questions)


async def all_tests(course_id: int = 1):
    tests = await TestDAO.find_all(course_id=course_id)
    if not tests:
        raise HTTPException(status_code=404, detail="No tests found")

    def build_test(test):
        return STest(
            id=test.id,
            name=test.name,
            course_id=test.course_id
        )

    return [build_test(test) for test in tests]

async def check_answer(test_id: int, question_id: int, selected_answer_id: int) -> bool:
    answer_to_question = await AnswerToQuestionDAO.find_one_or_none(
        test_id=test_id, question_id=question_id, answer_id=selected_answer_id
    )
    if not answer_to_question:
        raise AnswerNotFound

    return answer_to_question.is_correct
