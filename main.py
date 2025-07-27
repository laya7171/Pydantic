from pydantic import BaseModel

class User(BaseModel):

    name: str
    age: int
    condition: str


def insert_data(patient: User):

    print(patient.name)
    print(patient.age)

    print("Inserted into database with validation and type checking")

def update_patient_date(patient1: User):

    print(f"Updating patient data for {patient1.name} with age {patient1.age}")


patient_info = {
    "name": "John Doe", 
    "age": 30,
    "condition": "Healthy"
}

patient1 = User(**patient_info)
insert_data(patient1)
update_patient_date(patient1)




    