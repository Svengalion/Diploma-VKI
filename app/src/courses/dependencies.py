from fastapi import HTTPException
from fastapi.responses import FileResponse
from app.src.exceptions import IncorrectLection
from app.src.courses.dao import CourseDAO
import os

from app.src.courses.schemas import SCourse


async def all_courses():
    courses = await CourseDAO.find_all()
    if not courses:
        raise IncorrectLection
    return [SCourse.from_orm(course) for course in courses]
