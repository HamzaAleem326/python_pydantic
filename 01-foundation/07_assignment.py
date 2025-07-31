"""
📘 ASSIGNMENT: Pydantic Advanced Features Practice

Tasks:
1. Create a `Product` model with the following:
   - id: UUID (auto-generated using `default_factory`)
   - name: non-empty string (with field validator)
   - price: float (must be greater than 0)
   - created_at: datetime (auto set with `default_factory`)
2. Use `Field` aliases (e.g., "product_id" instead of "id")
3. Apply model-level validator to log before and after validation
4. Print the model as dict and JSON
"""

from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict  # type: ignore
from uuid import uuid4
from datetime import datetime

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="product_id")
    name: str
    price: float = Field(..., gt=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )

    @field_validator("name")
    @classmethod
    def name_cannot_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Product name cannot be empty")
        return value.title()

    @model_validator(mode="before")
    @classmethod
    def before_validation(cls, data):
        print("Before validation triggered")
        return data

    @model_validator(mode="after")
    def after_validation(self):
        print("After validation triggered")
        return self

# Create and test product
product = Product(name="graphics card", price=1500.0)

# Output
print(product.model_dump())
print(product.model_dump_json(indent=2))

# Trigger assignment validation
product.name = "updated product"
print(product.name)
