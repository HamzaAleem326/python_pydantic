"""
🧠 NOTES: Pydantic Validators and Computed Fields

This note covers:
1. field_validator – for validating single fields
2. model_validator – for validating across multiple fields
3. computed_field – for generating derived fields from model data
"""

from pydantic import BaseModel, field_validator, model_validator, computed_field  # type: ignore

# ----------------------------------
# ✅ 1. Field Validator
# ----------------------------------

class User(BaseModel):
    user_name: str

    @field_validator('user_name')
    def user_name_length(cls, v):
        if len(v) < 4:
            raise ValueError('username must be at least 4 characters long')
        return v

# ✅ Example
try:
    User(user_name="bob")  # Too short, will raise error
except ValueError as e:
    print(f"❌ User validation error: {e}")

user = User(user_name="bobby")
print(f"✅ Valid user: {user}")

# ----------------------------------
# ✅ 2. Model Validator
# ----------------------------------

class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('passwords do not match')
        return values

# ✅ Example
try:
    SignUpData(password="secret123", confirm_password="secret124")
except ValueError as e:
    print(f"\n❌ Signup validation error: {e}")

signup = SignUpData(password="secret123", confirm_password="secret123")
print(f"✅ Valid signup: {signup}")

# ----------------------------------
# ✅ 3. Computed Field
# ----------------------------------

class Product(BaseModel):
    name: str
    price: float
    quantity: int = 1

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

# ✅ Example
product = Product(name="Laptop", price=999.99, quantity=2)
print(f"\n💰 Product total: {product.total_price}")