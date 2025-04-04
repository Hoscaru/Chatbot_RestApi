from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int

class UserForm(BaseModel):
    name: str
    age: int
    email: str
    direction: str

class Prompt(BaseModel):
    prompt: str

