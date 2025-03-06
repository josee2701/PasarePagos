
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str
    
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    password: str = Field(max_length=100)
    email: EmailStr = Field(max_length=100)
    address: str = Field(max_length=100, nullable=True)
    phone: int | None = Field(default=None, nullable=True)