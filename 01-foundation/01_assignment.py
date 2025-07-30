from pydantic import BaseModel # type:ignore

# todo: create a product model with id,name,price,instock

class Product(BaseModel):
    id:int
    name:str
    price:float
    instock:bool = True # we can also add default value


GPU = {'id':101, 'name':'Nvidia Rtx 5090', 'price':2000, 'instock':True}
product = Product(**GPU)
print(product)

CPU = {'id':102, 'name':'Intel i9 14900K', 'price':600, 'instock':False}
cpu_product = Product(**CPU)
print(cpu_product)