
from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel):
    name: str = Field(max_length=100)
    password: str = Field(max_length=100)
    email: EmailStr = Field(max_length=100)
    address: str = Field(max_length=100, nullable=True)
    phone: int | None = Field(default=None, nullable=True)
    accountNumber: str = Field(max_length=100)

class UserTable(User, table=True,):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserCreate(User):
    pass
    