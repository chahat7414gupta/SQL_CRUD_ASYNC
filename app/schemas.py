from pydantic import BaseModel
from typing import Optional, List

class MessageCreate(BaseModel):
    content: str
    user_id: int

class MessageRead(BaseModel):
    id: int
    content: str
    user_id: int

    class Config:
        orm_mode = True

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    messages: List[MessageRead] = []

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str


