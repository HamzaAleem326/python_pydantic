"""
📝 ASSIGNMENT: User Registration with Validation
- Create a user registration model using Pydantic
- Validate name length, email format, and age range using Field() and conint()
- Add custom validation to check for banned email domains
"""

from pydantic import BaseModel, Field, EmailStr, conint, field_validator  # type: ignore
from typing import List

class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    age: conint(gt=0, lt=150)  # age must be > 0 and < 150

    @field_validator('email')
    @classmethod
    def block_free_email_domains(cls, v: str) -> str:
        banned_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
        domain = v.split('@')[-1]
        if domain in banned_domains:
            raise ValueError(f"Registration using {domain} is not allowed.")
        return v

# Valid user
try:
    user = User(name="Hamza", email="hamza@protonmail.com", age=22)
    print("✅ Valid user:")
    print(user)
except Exception as e:
    print("❌ Error creating valid user:")
    print(e)

print("\n" + "="*40 + "\n")

# Invalid user (blocked email domain)
try:
    user = User(name="Ali", email="ali@gmail.com", age=25)
    print(user)
except Exception as e:
    print("❌ Validation error for blocked domain:")
    print(e)

print("\n" + "="*40 + "\n")

# Invalid user (too short name)
try:
    user = User(name="A", email="short@example.com", age=30)
    print(user)
except Exception as e:
    print("❌ Validation error for name:")
    print(e)

print("\n" + "="*40 + "\n")

# Invalid user (age out of range)
try:
    user = User(name="Zara", email="zara@example.com", age=151)
    print(user)
except Exception as e:
    print("❌ Validation error for age:")
    print(e)

print("\n" + "="*40 + "\n")