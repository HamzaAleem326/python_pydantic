"""
🧠 NOTES: Basic Pydantic Model
Pydantic is a Python library used to validate and serialize data using Python type hints.
It is commonly used with FastAPI and other modern Python tools.
"""

from pydantic import BaseModel  # type: ignore

# ✅ Defining a basic model
class User(BaseModel):
    id: int           # Integer field
    name: str         # String field
    is_active: bool   # Boolean field

# ✅ Automatic type conversion
valid_data = {'id': '101', 'name': 'John', 'is_active': 1}
user = User(**valid_data)  # Converts '101' → int and 1 → bool
print(f"✅ Valid user data: {user}")

# ❌ Handling invalid data
try:
    invalid_data = {'id': 'not_a_number', 'name': 123, 'is_active': 'maybe'}
    User(**invalid_data)
except Exception as e:
    print(f"\n❌ Validation error:\n{e}")

# 🔁 Serialization to dict and JSON
print(f"\n📦 Model to dict: {user.model_dump()}")
print(f"📦 Model to JSON: {user.model_dump_json()}")
