"""
🎯 ASSIGNMENT: Create and use a basic Pydantic model

TASKS:
1. Create a Product model using Pydantic with the following fields:
    - id: int
    - name: str
    - price: float
    - instock: bool (default should be True)
2. Create two dictionaries representing different products.
3. Use the Product model to validate these dictionaries.
4. Print the validated Product instances.
"""

from pydantic import BaseModel  # type: ignore

# ✅ Step 1: Define the Product model
class Product(BaseModel):
    id: int
    name: str
    price: float
    instock: bool = True  # Default value

# ✅ Step 2: Create dictionaries representing product data
GPU = {'id': 101, 'name': 'Nvidia RTX 5090', 'price': 2000, 'instock': True}
CPU = {'id': 102, 'name': 'Intel i9 14900K', 'price': 600, 'instock': False}

# ✅ Step 3: Use Pydantic model to validate data
product_gpu = Product(**GPU)
product_cpu = Product(**CPU)

# ✅ Step 4: Print the validated models
print(product_gpu)
print(product_cpu)