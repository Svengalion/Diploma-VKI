from pydantic import BaseModel


class SLection(BaseModel):
    name: str
    description: str
    file_path: str

    class Config:
        orm_mode = True
        from_attributes = True