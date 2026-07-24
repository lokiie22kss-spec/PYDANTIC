from pydantic import BaseModel, EmailStr, AnyUrl,  Field, field_validator
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
    
    #check if the patient is an employee of hdfc /icici bank, if yes then only allow the email address to be used for registration
    @field_validator('email') 
    #pass the field name to the decorator, so that we can use it in the validator function
    @classmethod
    #field_validator is a decorator provided by Pydantic.The function underneath it is expected to be a class method.
    #cls is a reference to the class itself and value is the value of the field being validated
    def email_validator(cls, value):
        print("value: ",value)
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@gmail.com
        #split on the basis of @ and get the last part of the email address which is the domain name
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
    
    #we want the ptient name to be stored in uppercase, so we can use a field validator to transform the name to uppercase
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        print("value: ",value)
        return value.upper()
    
    #we want to validate the age of the patient, so we can use a field validator to check if the age is between 0 and 100
    #field validator has two modes, before and after, before mode is used to validate the field before it is set and after mode is used to validate the field after type coersion
    @field_validator('age', mode='after')
    #Pydantic calls validator  after type conversion.i.e. if the age is passed as a string, it will be converted to an integer before the validator is called.
    #if before mode is used, the validator will be called before type conversion and the value will be a string in this case.
    @classmethod
    def validate_age(cls, value):
        print("value: ",value)
        print("value.type",type(value))
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


def update_patient_data(patient: Patient):

    # print(patient.name)
    # print(patient.age)
    # print(patient.allergies)
    # print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion
#Type Coercion means "30" --> 30
update_patient_data(patient1)

