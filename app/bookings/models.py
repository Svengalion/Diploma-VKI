from sqlalchemy import Column, Integer, JSON, String, ForeignKey, Date, Computed

from app.database import Base


class Bookings(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"))
    total_days = Column(Integer, Computed("(date_to - date_from)"))