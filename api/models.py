from typing import Optional

from pydantic import BaseModel


class CreateStudent(BaseModel):
    name: str
    email: Optional[str] = None


class Student(BaseModel):
    id: int
    name: str
    email: Optional[str] = None

    class Config:
        orm_mode = True
