from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.src.lections.schemas import SLection
from app.src.models import Lection, Result, User
from app.src.lections.dependencies import current_lection, all_lections, lection_pdf
from app.src.results.dependencies import get_user_results, update_user_result
from app.src.results.schemas import SResult, SUpdateResult
from app.src.users.dependencies import current_user

router = APIRouter(
    prefix="/results",
    tags=["Results"],
)


@router.get("/", response_model=List[SResult])
async def read_results(user: User = Depends(current_user)):
    return await get_user_results(user)


@router.put("/{test_id}/result")
async def update_result(test_id: int, update_data: int, user: User = Depends(current_user)):
    return await update_user_result(test_id, update_data, user)
