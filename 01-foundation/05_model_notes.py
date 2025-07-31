"""
🧠 NOTES: Advanced Pydantic Concepts
- Working with datetime fields
- Nested models with lists
- Custom JSON encoders using model_config
"""

from pydantic import BaseModel, ConfigDict  # type: ignore
from typing import List
from datetime import datetime  

# ✅ Nested Model: Address
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# ✅ Parent Model: Person
class Person(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    addresses: List[Address]
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime('%d %m %Y')  # ✅ Corrected: strftime, not datetime
        }
    )

# ✅ Creating a person instance
user = Person(
    id=1,
    name="Hamza",
    email="hamza@123hottail.coma",
    created_at=datetime.now(),
    is_active=True,
    addresses=[
        Address(
            street="123 Main St",
            city="Japan",
            zip_code="12334"
        )
    ],
    tags=['premium', 'subscriber']
)

# ✅ Serialize to dictionary
python_dict = user.model_dump()
print(python_dict)

print('=================================')

# ✅ Serialize to JSON string
json_string = user.model_dump_json()
print(json_string)