from fastapi import HTTPException
from fastapi.responses import FileResponse
from app.src.exceptions import IncorrectLection
from app.src.lections.dao import LectionDAO
import os

from app.src.lections.schemas import SLection


async def current_lection(id: int):
    lection = await LectionDAO.find_by_id(int(id))
    if not lection:
        raise IncorrectLection
    return lection


async def all_lections(course_id: int):
    lections = await LectionDAO.find_all(course_id=course_id)
    if not lections:
        raise IncorrectLection
    return [SLection.from_orm(lection) for lection in lections]


async def lection_pdf(id: int):
    lection = await current_lection(id)
    file_path = lection.file_path
    if not os.path.exists(file_path):
        raise IncorrectLection
    return FileResponse(path=file_path, filename=os.path.basename(file_path), media_type='application/pdf')
