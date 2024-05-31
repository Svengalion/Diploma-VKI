from fastapi import HTTPException, Depends
from fastapi.responses import FileResponse
from app.src.exceptions import IncorrectLection, ResultsNotFound, TestNotFound
from app.src.lections.dao import LectionDAO
import os

from app.src.lections.schemas import SLection
from app.src.models import User, Test
from app.src.results.dao import ResultDAO
from app.src.results.schemas import SResult, SUpdateResult
from app.src.users.dependencies import current_user
from app.src.tests.dao import TestDAO


async def get_user_results(user: User):
    results = await ResultDAO.find_by_user_id(user.id)
    if not results:
        raise ResultsNotFound
    return [SResult.from_orm(result) for result in results]


async def update_user_result(test_id: int, update_data: int, user: User):
    test = await TestDAO.find_by_id(test_id)
    if not test:
        raise TestNotFound
    result = await ResultDAO.find_by_user_and_test_id(user.id, test_id)
    if result:
        await ResultDAO.update(result.id, result=update_data)
        return {"message": "Result updated successfully"}
    else:
        await ResultDAO.insert_data(student_id=user.id, test_id=test_id, result=update_data)
        return {"message": "Result created successfully"}