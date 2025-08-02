# 🚀 Pydantic Crash Course – Notes & Assignments

Welcome to my personal journey through **Pydantic** – a powerful Python library used for **data validation**, **settings management**, and **type enforcement**, often used with frameworks like **FastAPI** and **Typer**.

This repository is a **well-structured collection** of learning notes and hands-on assignments that walk through essential and advanced features of **Pydantic v2+**.

---

## 📘 What is Pydantic?

**Pydantic** is a data validation and parsing library that uses Python type hints. It lets you define structured models with automatic type checking, default values, nested structures, and custom validation—all with **clear error messages**.

✨ You get:
- Type-safe data models
- Auto-validation of user input
- Easy JSON serialization/deserialization
- Integration with tools like FastAPI

---

## 📚 What's Included in This Tutorial?

Each tutorial consists of:
- ✅ A `XX_model_notes.py` file → detailed code-based notes
- 🧪 A `XX_assignment.py` file → hands-on practice with validation logic

| Part | Topic                         | Notes File           | Assignment File         |
|------|-------------------------------|----------------------|-------------------------|
| 01   | Intro to BaseModel            | `01_model_notes.py`  | `01_assignment.py`      |
| 02   | Lists, Dicts, Optionals       | `02_model_notes.py`  | `02_assignment.py`      |
| 03   | Validators & Computed Fields  | `03_model_notes.py`  | `03_assignment.py`      |
| 04   | Nested Models & Recursion     | `04_model_notes.py`  | `04_assignment.py`      |
| 05   | Datetime, JSON, and Config    | `05_model_notes.py`  | `05_assignment.py`      |
| 06   | FastAPI + Pydantic Basics     | `06_model_notes.py`  | `06_assignment.py`      |
| 07   | Aliases, Default Factory, Modes | `07_model_notes.py` | `07_assignment.py`      |
| 08   | Enum, Literal, Union Types    | `08_model_notes.py`  | `08_assignment.py`      |

---

## 🛠️ How to Use This Repo

Clone the repo and run any notes or assignment file using Python 3.10+.

```bash
git clone https://github.com/your-username/pydantic-tutorial.git
cd pydantic-tutorial

# Run any file
python 03_model_notes.py
python 06_assignment.py
