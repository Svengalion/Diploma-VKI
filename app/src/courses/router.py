from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.src.courses.schemas import SCourse
from app.src.models import Course
from app.src.courses.dependencies import all_courses

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)

@router.get("/", response_model=List[SCourse])
async def read_courses(skip: int = 0, limit: int = 10, courses: List[Course] = Depends(all_courses)):
    return courses
