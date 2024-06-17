from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.src.courses.schemas import SCourseId
from app.src.lections.schemas import SLection, SLectionId
from app.src.models import Lection, Course
from app.src.lections.dependencies import current_lection, all_lections, lection_pdf

router = APIRouter(
    prefix="/lections",
    tags=["Lections"],
)


@router.post("/", response_model=List[SLection])
async def read_lections(course_id: SCourseId):
    return await all_lections(course_id.id)


@router.get("/{lection_id}", response_model=SLection)
async def read_lection(lection: Lection = Depends(current_lection)):
    return lection


@router.post("/pdf")
async def get_lection_pdf(lection: SLectionId):
    return await lection_pdf(lection.id)
