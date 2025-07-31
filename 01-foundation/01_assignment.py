# Pydantic's BaseModel provides data validation, serialization and documentation features
from pydantic import BaseModel # type:ignore

class Product(BaseModel):
    # Field types are used by Pydantic for automatic validation
    id: int
    name: str
    price: float
    instock: bool = True  # Fields can have default values

# Pydantic will validate these dictionaries against the Product model
GPU = {'id':101, 'name':'Nvidia Rtx 5090', 'price':2000, 'instock':True}
product = Product(**GPU)
print(product)

CPU = {'id':102, 'name':'Intel i9 14900K', 'price':600, 'instock':False}
cpu_product = Product(**CPU)
print(cpu_product)