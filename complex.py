from pydantic import BaseModel
from typing import List, Dict


class User(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    alergy: list[str] #we can't use the normal list here because it doesn't enforce type checking
    contact_number: dict[str, str]  # Dictionary with string keys and values


user_info = {
    "name": "John Doe",
    "age": 30,
    "weight": 70.5,
    "married": True,
    "alergy": ["pollen", "nuts"],
    "contact_number": {
        "home": "123-456-7890",
        "work": "098-765-4321"
    }
}

user1 = User(**user_info)

def insert_user_data(user: User):
    print(f"Name: {user.name}")
    print(f"Age: {user.age}")
    print(f"Weight: {user.weight}")
    print(f"Married: {user.married}")
    print(f"Alergies: {', '.join(user.alergy)}")
    print(f"Contact Numbers: {user.contact_number}")
    print(f"user contact home {user.contact_number['home']}")

    print("Inserted into database with validation and type checking")


insert_user_data(user1)