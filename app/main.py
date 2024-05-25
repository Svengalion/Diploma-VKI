from datetime import datetime, date

from fastapi import FastAPI, Query, Depends
from typing import Optional, List
from pydantic import BaseModel
from app.users.router import router as router_users

app = FastAPI()
app.include_router(router_users)


class HotelsSearchArgs:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: bool | None = None
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels", response_model=List[SHotel])
async def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    return search_args

# class SBooking(BaseModel):
#     room_id: int
#     date_from: date
#     date_to: date
#
# @app.post("/bookings")
# async def add_bookings(booking: SBooking):
#     pass
