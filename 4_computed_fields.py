from pydantic import BaseModel, EmailStr, computed_field, model_validator
#field_validator--> allows custom validation of the fields
from typing import Optional, Annotated

class Patient(BaseModel):

    name : str
    email : EmailStr
    age: int
    height: float 
    weight: float
    married: bool
    allergies: list[str] 
    contact_details: dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        #BMI = weight(kg) / height(m)^2
        bmi = self.weight / (self.height ** 2)
        print("BMI: ", bmi)
        return round(bmi, 2) #round upto 2 decimal places

    

def update_patient_data(patient: Patient):

    # print(patient.name)
    # print(patient.age)
    # print(patient.allergies)
    # print(patient.married)
    print('BMI: ', patient.calculate_bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '24', 'height': 1.55, 'weight': 67, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}} 


patient1 = Patient(**patient_info) 
update_patient_data(patient1)

