from pydantic import BaseModel, Field # type: ignore
from typing import Optional

class Employee(BaseModel):
    id:int
    name:str = Field(
        ..., # when something is mandatory
        min_length=3,
        max_length=20,
        description_name='Name of the employee'
        example='Hamza Aleem'
        )
    department:Optional[str] = 'general'
    salary:float = Field(..., gt=0) # gt means greater than zero
    email:str = Field(..., regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
     # regex means regular expression