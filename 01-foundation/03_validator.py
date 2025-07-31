# Demonstrating three types of Pydantic validators:
# 1. field_validator: Validates individual fields
# 2. model_validator: Validates multiple fields together
# 3. computed_field: Derives new fields from existing data

from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore

class User(BaseModel):
    user_name: str

    # field_validator: validates a single field
    @field_validator('user_name')
    def user_name_length(cls, v):
        if len(v) < 4:
            raise ValueError('username must be at least 4 characters long')
        return v

# Example usage of field_validator
try:
    user = User(user_name="bob")  # Will raise error
except ValueError as e:
    print(f"User validation error: {e}")

user = User(user_name="bobby")  # Will work
print(f"Valid user: {user}")

class SignUpData(BaseModel):
    password: str
    confirm_password: str
    
    # model_validator: validates multiple fields together
    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('passwords do not match')
        return values

# Example usage of model_validator
try:
    signup = SignUpData(password="secret123", confirm_password="secret124")
except ValueError as e:
    print(f"\nSignup validation error: {e}")

signup = SignUpData(password="secret123", confirm_password="secret123")
print(f"Valid signup: {signup}")

class Product(BaseModel):
    name: str
    price: float
    quantity: int = 1  # Adding quantity field with default value
    
    # computed_field: calculates a value based on other fields
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

# Example usage of computed_field
product = Product(name="Laptop", price=999.99, quantity=2)
print(f"\nProduct total: {product.total_price}")
     