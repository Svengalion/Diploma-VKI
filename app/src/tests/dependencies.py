from fastapi import Depends, HTTPException
from sqlalchemy import select
from app.src.tests.dao import TestDAO
from app.src.tests.schemas import STest
from app.src.models import Test
from app.src.database import async_session_maker


async def current_test(test_id: int):
    test = await TestDAO.find_with_details(test_id)
    if not test:
        raise HTTPException(status_code=404, detail="Test not found")
    return STest.from_orm(test)


async def all_tests(skip: int = 0, limit: int = 10):
    async with async_session_maker() as session:
        query = select(Test).offset(skip).limit(limit)
        result = await session.execute(query)
        tests = result.scalars().all()

        if not tests:
            raise HTTPException(status_code=404, detail="No tests found")
        return [STest.from_orm(test) for test in tests]
