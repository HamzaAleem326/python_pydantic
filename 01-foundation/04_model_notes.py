"""
🧠 NOTES: Pydantic Nested Models

This note covers:
- Creating nested data models (models inside models)
- Forward references for recursive relationships (like comments with replies)
"""

from pydantic import BaseModel  # type: ignore
from typing import List, Optional

# ----------------------------------
# ✅ 1. Basic Nested Model
# ----------------------------------

class Address(BaseModel):
    street: str
    city: str
    zip_code: str
    country: str

class Person(BaseModel):
    id: Optional[str] = None
    name: str
    age: int
    addresses: List[Address]  # A person can have multiple addresses

# ✅ Example: Create a nested structure
address = Address(
    street='123 Main St',
    city='New York',
    zip_code='10001',
    country='USA'
)

user = Person(
    id='12345',
    name='John Doe',
    age=30,
    addresses=[address]
)

print(f"🏠 Nested user: {user}")

# ----------------------------------
# ✅ 2. Recursive Models (Forward Reference)
# ----------------------------------

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # Refers to itself

# Required for forward references
Comment.model_rebuild()

# ✅ Example: Nested comments
comment = Comment(
    id=1,
    content='First comment',
    replies=[
        Comment(id=2, content='Thanks for sharing!')
    ]
)

print(f"\n💬 Nested comment thread: {comment}")