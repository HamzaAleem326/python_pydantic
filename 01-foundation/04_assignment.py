"""
🎯 ASSIGNMENT: Create a nested model for an online course platform

TASKS:
1. Define a Lesson model with:
   - id: int
   - title: str
   - content: str

2. Define a Module model that contains:
   - id: int
   - title: str
   - description: Optional[str]
   - lessons: List[Lesson]

3. Define a Course model that contains:
   - id: int
   - title: str
   - description: Optional[str]
   - modules: List[Module]

4. Create one course instance with nested modules and lessons.
5. Print the final nested Course model.
"""

from pydantic import BaseModel  # type: ignore
from typing import Optional, List

# ✅ Step 1: Define Lesson model
class Lesson(BaseModel):
    id: int
    title: str
    content: str

# ✅ Step 2: Define Module model with a list of lessons
class Module(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    lessons: List[Lesson] = []

# ✅ Step 3: Define Course model with a list of modules
class Course(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    modules: List[Module] = []

# ✅ Step 4: Create nested data
lesson1 = Lesson(id=1, title="Intro to Python", content="Variables, data types, and printing.")
lesson2 = Lesson(id=2, title="Control Flow", content="if, else, loops.")

module1 = Module(id=1, title="Python Basics", description="Learn the fundamentals of Python.", lessons=[lesson1, lesson2])

course = Course(
    id=101,
    title="Complete Python Course",
    description="A beginner-friendly course on Python programming.",
    modules=[module1]
)

# ✅ Step 5: Print the nested structure
print(f"📚 Full course data:\n{course}")