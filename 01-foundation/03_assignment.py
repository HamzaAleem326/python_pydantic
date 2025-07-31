"""
🎯 ASSIGNMENT: Use Pydantic validators and computed fields

TASKS:
1. Create a Booking model with:
   - user_id: str
   - room_id: int
   - nights: int (must be ≥ 1)
   - rate_per_night: float

2. Use Field to enforce the constraint on nights.
3. Add a computed field called total_cost that multiplies nights × rate_per_night.
4. Create an instance and print total_cost.
"""

from pydantic import BaseModel, Field, computed_field  # type: ignore

# ✅ Step 1: Define the model
class Booking(BaseModel):
    user_id: str
    room_id: int
    nights: int = Field(..., ge=1)  # Must be at least 1
    rate_per_night: float

    # ✅ Step 2: Computed field for total cost
    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night

# ✅ Step 3: Create instance and print result
booking = Booking(user_id="U001", room_id=101, nights=3, rate_per_night=1200.50)
print(f"💵 Total Booking Cost: {booking.total_cost}")