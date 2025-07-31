"""
🎯 ASSIGNMENT: Build a FastAPI app using Pydantic and Dependency Injection

TASKS:
1. Create a FastAPI app instance.
2. Define a UserSignup Pydantic model with:
   - username: str
   - email: EmailStr
   - password: str

3. Define a Settings model with:
   - app_name: str (default: "Assignment App")
   - admin_email: EmailStr (default: "admin@assignment.com")

4. Create a dependency function that returns an instance of Settings.

5. Add a POST route `/signup` to accept user signup data.
   Return a success message using the username.

6. Add a GET route `/settings` that uses the dependency and returns settings.
"""

from fastapi import FastAPI, Depends  # type: ignore
from pydantic import BaseModel, EmailStr  # type: ignore

app = FastAPI()

# ✅ Step 2: Signup model
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

# ✅ Step 3: Settings model
class Settings(BaseModel):
    app_name: str = "Assignment App"
    admin_email: EmailStr = "admin@assignment.com"

# ✅ Step 4: Dependency
def get_settings():
    return Settings()

# ✅ Step 5: Signup route
@app.post("/signup")
def signup(user: UserSignup):
    return {"message": f"User {user.username} created successfully"}

# ✅ Step 6: Settings route
@app.get("/settings")
def settings_route(settings: Settings = Depends(get_settings)):
    return settings
