from fastapi import APIRouter, Depends
from typing import List

from app.src.courses.schemas import SCourseId
from app.src.tests.schemas import STest, STestQuests, STestId, SCheck
from app.src.models import Test
from app.src.tests.dependencies import current_test, all_tests, check_answer

router = APIRouter(
    prefix="/tests",
    tags=["Tests"],
)


@router.post("/", response_model=List[STest])
async def read_tests(course_id: SCourseId):
    return await all_tests(course_id.id)


@router.post("/{test_id}", response_model=STestQuests)
async def read_test(testID: STestId):
    return await current_test(testID.id)


@router.post("/{test_id}/{question_id}/check-answer")
async def check_answer_endpoint(test: SCheck):
    return await check_answer(test.test_id, test.question_id, test.selected_answer_id)
