"""
🧠 NOTES: Pydantic with Complex Data Types

This covers how to use Pydantic with:
- Lists and Dictionaries with type constraints
- Optional fields with default values
- Nested model validation
"""

from pydantic import BaseModel  # type: ignore
from typing import List, Dict, Optional

# ✅ Model with list and dictionary types
class Cart(BaseModel):
    user_id: int
    items: List[str]              # List of strings
    quantities: Dict[str, int]    # Dictionary: item_name → quantity

# ✅ Example with valid data
cart_data = {
    "user_id": 1,
    "items": ["book", "laptop", "coffee"],
    "quantities": {"book": 2, "laptop": 1, "coffee": 3}
}
cart = Cart(**cart_data)
print(f"✅ Valid cart: {cart}")

# ❌ Example with invalid data (wrong types)
try:
    invalid_cart = {
        "user_id": 1,
        "items": ["book", 123],           # 123 is not a string
        "quantities": {"book": "two"}     # "two" is not an int
    }
    Cart(**invalid_cart)
except Exception as e:
    print(f"\n❌ Cart validation error:\n{e}")

# ✅ Optional fields with default value
class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None  # Optional field, defaults to None

# ✅ Blog post examples
post_with_image = BlogPost(
    title="Hello",
    content="World",
    image_url="https://example.com/image.jpg"
)
post_without_image = BlogPost(
    title="Hello",
    content="World"
)

print(f"\n🖼️ Post with image: {post_with_image}")
print(f"📝 Post without image: {post_without_image}")