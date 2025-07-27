from pydantic import BaseModel, Field , field_validator , model_validator , computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    age: int 
    email: str
    weight: float
    height: int
    married: bool
    allergies: List[str]
    contact_detail: Dict[str, str]

    @computed_field
    @property
    def compute_bmi(self)-> float:
        return self.weight / ((self.height / 100) ** 2)

    @field_validator('email')
    @classmethod
    def email_validator(cls, value: str):

        valid_domain = ["everest.com", "prabhu.com" ]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError(f"Invalid email domain: {domain_name}. Allowed domains are {valid_domain}")
        else:
            return value

    @field_validator('name') #there are 2 types of modes in field validator, one is before and the other is after
    @classmethod
    def name_validator(cls, value: str):
        
        return value.lower() # we lowercase the name for consistency
    
    @field_validator('age', mode = 'after')
    @classmethod
    def validate_age(cls, age_value: int):
        if 0 < age_value < 100: 
            return age_value
        else: 
            raise ValueError("Age must be between 1 and 99") #this function will perform simple validation 
        #if we use before mode, and someone enters a string as 'thirty', it will raise a validation error
        #if we use after mode, it will convert the string to an intege and then check if condition 

    #now we will use model validator to validate if the patient is over 60 it should have emergency contact details
    @model_validator(mode = 'after')
    @classmethod
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_detail:
            raise ValueError("Patients over 60 must have emergency contact details")
        return model


def update_patient_data(patient: Patient):
    print(f"Updating patient data for {patient.name} with age {patient.age}")
    print(f"Weight: {patient.weight}, Married: {patient.married}")
    print(f"Allergies: {', '.join(patient.allergies) if patient.allergies else 'None'}")
    print(f"BMI: {patient.compute_bmi:.2f}")
    print(f"Contact Details: {patient.contact_detail}")


patient_info = {
    "name": "Jane Doe",
    "age": 70,
    "weight": 65.5,
    "height": 165,
    "married": False,
    "email": "jane.doe@everest.com",
    "allergies": ["Peanuts", "Dust"],
    "contact_detail": {
        "home": "123-456-7890",
        "work": "098-765-4321",
        "emergency": "911"
    }
}

patient1 = Patient(**patient_info)

update_patient_data(patient1)