from pydantic import BaseModel, EmailStr, model_validator
#field_validator--> allows custom validation of the fields
from typing import Optional, Annotated

class Patient(BaseModel):

    name : str
    email : EmailStr
    age: int
    weight: float
    married: bool
    allergies: list[str] 
    contact_details: dict[str, str]

    #check if the age is greater than 60 then there should be an emergency contact number provided in the contact_details dictionary
    #here we can't use field_validator because we need to validate two fields together, so we can use model_validator instead
    @model_validator(mode='after')
    #@classmethod   --> READ why there is no classmethod decorator 
    def validate_emergency_contact(cls, model):
        #here we are passing the entire model to the validator function, so we can access all the fields of the pydantic model
        print("model: ", model)
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients above 60 years of age')
        return model

def update_patient_data(patient: Patient):

    # print(patient.name)
    # print(patient.age)
    # print(patient.allergies)
    # print(patient.married)
    print('updated')

#patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}  --> this is going to run without any error because the age is less than 60 

#patient_info = {'name':'nitish', 'email':'abcnjdn@gmail.com', 'age': '70', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}  #--> this is going to give validation error because the age is greater than 60 and there is no emergency contact number provided in the contact_details dictionary

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '70', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency_contact':'9876543210'}}  #--> this is going to run without any error because the age is greater than 60 and there is an emergency contact number provided in the contact_details dictionary
patient1 = Patient(**patient_info) 
update_patient_data(patient1)

