from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.src.lections.schemas import SLection
from app.src.models import Lection
from app.src.lections.dependencies import current_lection, all_lections, lection_pdf

router = APIRouter(
    prefix="/lections",
    tags=["Lections"],
)


@router.get("/", response_model=List[SLection])
async def read_lections(skip: int = 0, limit: int = 10, lections: List[Lection] = Depends(all_lections)):
    return lections


@router.get("/{lection_id}", response_model=SLection)
async def read_lection(lection: Lection = Depends(current_lection)):
    return lection


@router.get("/{lection_id}/pdf")
async def get_lection_pdf(lection_id: int):
    return await lection_pdf(lection_id)
