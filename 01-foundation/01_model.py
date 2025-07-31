# Pydantic is a data validation library that:
# 1. Validates data types at runtime
# 2. Provides automatic data parsing
# 3. Helps catch errors early with clear error messages
# 4. Enables easy data serialization/deserialization

from pydantic import BaseModel # type: ignore

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# Pydantic automatically validates types and converts data when possible
valid_data = {'id': '101', 'name': 'John', 'is_active': 1}  # Note: string '101' and int 1
user = User(**valid_data)  # Pydantic converts '101' to int and 1 to bool
print(f"Valid data example: {user}")

# Pydantic raises validation errors for invalid data
try:
    invalid_data = {'id': 'not_a_number', 'name': 123, 'is_active': 'maybe'}
    User(**invalid_data)
except Exception as e:
    print(f"\nValidation error example:\n{e}")

# Pydantic models can be converted to dict/json
print(f"\nModel to dict: {user.model_dump()}")  # Convert to dictionary
print(f"Model to JSON: {user.model_dump_json()}")  # Convert to JSON string