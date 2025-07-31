"""
🧠 NOTES: Pydantic Advanced Features
- Using default_factory for dynamic default values
- Aliases for field names (e.g., user_id instead of id)
- Field-level and model-level validators
- Custom model configuration using ConfigDict
"""

from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict  # type: ignore
from typing import Optional
from datetime import datetime
import uuid

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="user_id")
    name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_default=True,
        validate_assignment=True,
        ser_json_timedelta="iso8601",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value.title()

    @model_validator(mode="before")
    @classmethod
    def pre_validator(cls, data):
        print("Running BEFORE model validation")
        return data

    @model_validator(mode="after")
    def post_validator(self):
        print("Running AFTER model validation")
        return self

# Create instance
user = User(name="hamza", email="hamza@example.com")

# Dump as dict
print(user.model_dump())

print("="*40)

# Dump as JSON
print(user.model_dump_json(indent=2))

# Test assignment validation
user.name = "ali"
print(user.name)
