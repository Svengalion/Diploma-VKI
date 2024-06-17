from pydantic import BaseModel


class SFeedback(BaseModel):
    feedback: str

    class Config:
        orm_mode = True
        from_attributes = True
