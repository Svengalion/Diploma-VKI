from pydantic import BaseModel


class SCourse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class SCourseId(BaseModel):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
