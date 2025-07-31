"""
🎯 ASSIGNMENT: Build a nested Pydantic model with datetime and custom JSON encoding

TASKS:
1. Create an Address model with:
   - street: str
   - city: str
   - zip_code: str

2. Create a Person model that includes:
   - id: int
   - name: str
   - email: str
   - is_active: bool (default: True)
   - created_at: datetime
   - addresses: List[Address]
   - tags: List[str] = []

3. Add a model_config to format datetime as 'DD MM YYYY' during JSON serialization.

4. Instantiate a Person object with nested Address list.

5. Print the model as a dict and as a JSON string.
"""

from pydantic import BaseModel, ConfigDict  # type: ignore
from typing import List
from datetime import datetime

# ✅ Step 1: Address model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# ✅ Step 2: Person model
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
            datetime: lambda v: v.strftime('%d %m %Y')
        }
    )

# ✅ Step 3: Create instance
person = Person(
    id=100,
    name="Sarah",
    email="sarah@example.com",
    created_at=datetime.now(),
    addresses=[
        Address(street="45 Park Ave", city="London", zip_code="W1A1AA")
    ],
    tags=["new", "vip"]
)

# ✅ Step 4: Output
print("📦 As dict:\n", person.model_dump())
print("\n🧾 As JSON:\n", person.model_dump_json())