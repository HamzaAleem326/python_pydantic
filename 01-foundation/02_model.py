# Demonstrating Pydantic's support for complex data types:
# - Lists and Dictionaries with type constraints
# - Optional fields with default values
# - Nested validation

from pydantic import BaseModel # type: ignore
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]        # Validates each item in the list is a string
    quantities: Dict[str, int]  # Validates keys are strings and values are integers

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # Optional field with None as default

# Example with Cart model
cart_data = {
    "user_id": 1,
    "items": ["book", "laptop", "coffee"],
    "quantities": {"book": 2, "laptop": 1, "coffee": 3}
}
cart = Cart(**cart_data)
print(f"Valid cart: {cart}")

# Example with invalid data
try:
    invalid_cart = {
        "user_id": 1,
        "items": ["book", 123],  # Invalid: contains non-string item
        "quantities": {"book": "two"}  # Invalid: value should be int
    }
    Cart(**invalid_cart)
except Exception as e:
    print(f"\nValidation error:\n{e}")

# Example with optional fields
post_with_image = BlogPost(
    title="Hello",
    content="World",
    image_url="https://example.com/image.jpg"
)
post_without_image = BlogPost(
    title="Hello",
    content="World"  # image_url will default to None
)
print(f"\nPost with image: {post_with_image}")
print(f"Post without image: {post_without_image}")


