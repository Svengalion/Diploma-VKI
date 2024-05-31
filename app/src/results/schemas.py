# app/src/results/schemas.py

from pydantic import BaseModel


class SResult(BaseModel):
    id: int
    student_id: int
    test_id: int
    result: int

    class Config:
        orm_mode = True
        from_attributes = True


class SUpdateResult(BaseModel):
    result: int
