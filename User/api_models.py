from .enums import *
from field_validations import *
from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

name = "^[a-zA-Z]+[a-zA-Z.\w]*$"
work_email = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
phone_number = "^\+\d+$"
topic = ".*"


class User(BaseModel):
    first_name: str
    last_name: str
    work_email: EmailStr
    phone_number: str
    topic: str
    date_of_birth: date
    interest: Interest
    gender: Gender

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        validate_field(self.first_name, 'first name', name, 30)
        validate_field(self.last_name, 'last name', name, 30)
        validate_field(self.work_email, 'work email', work_email, 60)
        validate_field(self.phone_number, 'phone number', phone_number, 60)
        validate_field(self.topic, 'topic', topic, 600)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "Abdul",
                "last_name": "Muhib",
                "work_email": "email@ili.digital",
                "phone_number": "+923244341224",
                "topic": "Fast Api learning",
                "date_of_birth": "2000-07-21",
                "interest": "Sports",
                "gender": "Male"
            }
        }


class UserOptional(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    work_email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    topic: Optional[str] = None
    date_of_birth: Optional[date] = None
    interest: Optional[Interest] = None
    gender: Optional[Gender] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.first_name:
            validate_field(self.first_name, 'first name', name, 30)
        if self.last_name:
            validate_field(self.last_name, 'last name', name, 30)
        if self.work_email:
            validate_field(self.work_email, 'work email', work_email, 60)
        if self.phone_number:
            validate_field(self.phone_number, 'phone number', phone_number, 60)
        if self.topic:
            validate_field(self.topic, 'topic', topic, 600)

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    work_email: EmailStr
    phone_number: str
    topic: str
    date_of_birth: date
    interest: Interest
    gender: Gender

    class Config:
        orm_mode = True
