from pydantic import BaseModel
from typing import List


class SAnswer(BaseModel):
    id: int
    answer: str

    class Config:
        orm_mode = True


class SQuestion(BaseModel):
    id: int
    question: str
    answers: List[SAnswer]

    class Config:
        orm_mode = True


class STest(BaseModel):
    id: int
    name: str
    questions: List[SQuestion]

    class Config:
        orm_mode = True
        from_attributes=True