from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    
    city: str
    state: str
    pin_code: str
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {
    "city": "Kathmandu",
    "state": "Bagmati",
    "pin_code": "44600"
}

address1 = Address(**address_dict)

patient_info = {
    "name": "laya",
    "age": 30,
    "gender": "female",
    "address": address1
}

patient1 = Patient(**patient_info)

temp = patient1.model_dump()

print(type(temp))
print(temp)

temp_json = patient1.model_dump_json()

#export the data to json file
with open("patient_data.json", "w") as file:
    file.write(temp_json)