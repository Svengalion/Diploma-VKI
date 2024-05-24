from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings
from app.database import async_session_maker
from app.bookings.schemas import SBooking
from app.users.dependencies import current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
async def get_bookings(user: Users = Depends(current_user)) -> Optional[list[SBooking]]:
    return await BookingDAO.find_all(user_id=user.id)

@router.post("")
async def add_booking(user: Users = Depends(current_user)):
    await BookingDAO.insert_data()