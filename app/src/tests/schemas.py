from pydantic import BaseModel
from typing import List


class SAnswer(BaseModel):
    id: int
    answer: str

    class Config:
        orm_mode = True
        from_attributes = True


class SQuestion(BaseModel):
    id: int
    question: str
    answers: List[SAnswer]

    class Config:
        orm_mode = True
        from_attributes = True


class STest(BaseModel):
    id: int
    name: str
    course_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class STestQuests(BaseModel):
    questions: List[SQuestion]

    class Config:
        orm_mode = True
        from_attributes = True


class STestId(BaseModel):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class SCheck(BaseModel):
    test_id: int
    question_id: int
    selected_answer_id: int

    class Config:
        orm_mode = True
        from_attributes = True
