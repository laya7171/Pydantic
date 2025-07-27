from pydantic import BaseModel , Field
from typing import List, Dict, Optional , Annotated

class User(BaseModel):

    name: Annotated[str, Field(default = "Guest", max_length=50, description = "Name of the user ")]  # Default value "Guest" with a max length of 50 characters
    email: str = Field(max_length=100)
    age: int = Field(ge=0)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default= False, description = "Is the user married?")]
    alergy: Optional[List[str]] = None #(The None is a default value)
    contact_number: Dict[str, str]  # Dictionary with string keys and values
    
    #we can't use the normal list here because it doesn't enforce type checking
    #by default, all the fields are required


user_info = {
    "name": "John Doe",
    "email": "abc@gmail.com",
    "age": 30,
    "weight": 70.5,
    "married": True,
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
    print(f"Alergies: {user.alergy}")
    print(f"Contact Numbers: {user.contact_number}")
    print(f"user contact home {user.contact_number['home']}")

    print("Inserted into database with validation and type checking")


insert_user_data(user1)