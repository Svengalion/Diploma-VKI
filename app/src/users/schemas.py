from pydantic import BaseModel


class SUserAuth(BaseModel):
    login: str
    password: str


class SUpdateUsername(BaseModel):
    name: str


class SUser(BaseModel):
    id: int
    login: str
    name: str | None = None
    image_path: str | None = None

    class Config:
        orm_mode = True
