# Field allows adding validations, metadata and constraints to model fields
from pydantic import BaseModel, Field # type: ignore
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,  # ... means this field is required (Pydantic's explicit way to mark required fields)
        min_length=3,  # Pydantic will validate minimum string length
        max_length=20, # Pydantic will validate maximum string length
        description='Name of the employee',  # Field metadata for documentation
        example='Hamza Aleem'  # Example value for documentation
    )
    department: Optional[str] = 'general'  # Optional field with default value
    salary: float = Field(..., gt=0)  # Validate salary is greater than 0