from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class User(Document):
    fullname: str
    email: EmailStr
    password: str

    class Collection:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Type here",
                "email": "xyz@solvyfi.com",
                "password": "123"
            }
        }


class UserSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "xyz@solvyfi.com",
                "password": "123"
            }
        }


class UserData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Type here",
                "email": "xyz@solvyfi.com",
            }
        }
