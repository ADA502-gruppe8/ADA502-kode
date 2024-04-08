from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str  # Or you can use an integer to represent roles and map them to actual roles in your application