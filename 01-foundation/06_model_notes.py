"""
🧠 NOTES: FastAPI + Pydantic Basics
- Request body validation using Pydantic models
- Dependency injection with FastAPI's Depends
"""

from fastapi import FastAPI, Depends  # type: ignore
from pydantic import BaseModel, EmailStr  # type: ignore

app = FastAPI()

# ✅ Model for user signup request
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

# ✅ Model for app settings
class Settings(BaseModel):
    app_name: str = "My FastAPI App"
    admin_email: EmailStr = "admin@example.com"

# ✅ Dependency function
def get_settings():
    return Settings()

# ✅ POST endpoint to accept signup data
@app.post('/signup')
def signup(user: UserSignup):
    return {'message': f'User {user.username} created successfully'}

# ✅ GET endpoint to return app settings
@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings