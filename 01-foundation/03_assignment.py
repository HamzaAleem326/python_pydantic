# Importing Pydantic components for model definition, field validation, and computed properties
from pydantic import BaseModel,Field,computed_field # type:ignore

class Booking(BaseModel):
    # Basic fields with type validation
    user_id: str
    room_id: int
    # Field with validation constraint: nights must be at least 1
    # ... indicates required field (no default value)
    nights: int = Field(..., ge=1)  
    rate_per_night: float 

    # Computed field that automatically calculates total cost
    # Updates whenever nights or rate_per_night changes
    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
