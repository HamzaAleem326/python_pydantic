"""
🧠 NOTES: Pydantic Models with Enum, Literal, Union, and Custom Types

- 🔘 Enum: Limit field values to a predefined set (e.g., Gender, Status)
- 🧾 Literal: Restrict values to fixed choices (useful for fixed states)
- ⚖️ Union: Accept multiple types for a single field (e.g., str | int)
- 🛠️ Custom Types: Define your own data types with validation rules
"""

from pydantic import BaseModel, Field, EmailStr, conint, field_validator  # type: ignore
from typing import Literal, Union
from enum import Enum
from uuid import UUID
from datetime import date 


# Gender Enum
class Gender(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

# User status using Literal
Status = Literal['active', 'inactive', 'banned']

# Custom Pydantic model
class User(BaseModel):
    id: UUID
    name: str
    age: conint(gt=0, lt=150)
    gender: Gender
    email: EmailStr
    status: Status
    birth_date: Union[date, str]  # Accept date object or string

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be blank")
        return value.title()

# Create a user
from uuid import uuid4
from datetime import datetime

user = User(
    id=uuid4(),
    name="hamza",
    age=24,
    gender="male",
    email="hamza@example.com",
    status="active",
    birth_date="2000-05-01"
)

print(user.model_dump())
