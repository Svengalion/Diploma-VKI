from pydantic import BaseModel


class SLection(BaseModel):
    name: str
    description: str
    file_path: str

class STask(BaseModel):
    id: int
    name: str