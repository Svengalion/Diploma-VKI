from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.src.courses.schemas import SCourse
from app.src.feedback.dependencies import put_feedback
from app.src.feedback.schemas import SFeedback
from app.src.models import Course
from app.src.courses.dependencies import all_courses

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"],
)

@router.put("/")
async def feedback(feed: SFeedback):
    return await put_feedback(feed.feedback)
