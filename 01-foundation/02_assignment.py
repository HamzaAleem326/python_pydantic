"""
🎯 ASSIGNMENT: Use Pydantic with field validation and optional fields

TASKS:
1. Create an Employee model with the following fields:
    - id: int
    - name: str (required, min 3 characters, max 20 characters)
    - department: Optional[str], defaults to 'general'
    - salary: float (must be greater than 0)
2. Use Pydantic's Field to define constraints and metadata.
3. Create an instance of Employee with valid data and print it.
"""

from pydantic import BaseModel, Field  # type: ignore
from typing import Optional

# ✅ Step 1: Define the model with validation
class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,  # Required field
        min_length=3,
        max_length=20,
        description="Name of the employee",
        example="Hamza Aleem"
    )
    department: Optional[str] = 'general'  # Optional with default
    salary: float = Field(..., gt=0)  # Must be > 0

# ✅ Step 2: Create valid employee instance
employee = Employee(
    id=1,
    name="Hamza Aleem",
    department="Engineering",
    salary=150000
)

# ✅ Step 3: Output the result
print(employee)