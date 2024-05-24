from sqlalchemy import Column, Integer, JSON, String

from app.database import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    number = Column(Integer)
    group = Column(String)
    role = Column(String)