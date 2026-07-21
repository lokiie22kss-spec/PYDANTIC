from pydantic import BaseModel, EmailStr,AnyUrl,Field
#Every Pydantic model must inherit from BaseModel.importing the BaseModel class from Pydantic. 
#from typing import List  --> this is require in older versions of Pydantic for defining list types, but in newer versions, you can use the built-in list type directly.
from typing import Optional, Annotated

#patient model is created 
class Patient(BaseModel):
    #creating a model for patient with name and age attributes
    # Annotated lets us attach extra validation rules and metadata to a data type.# The actual type remains 'str'; Field() simply adds constraints like max_length and descriptions.
    name: Annotated[ str , Field(max_length=50,description="Name of the pateidn less than 50 characters",examples=["Suman"]) ] 
     #Field is used to add additional validation and metadata to the name attribute. Here, it specifies that the maximum length of the name should be 50 characters.
    age: int = Field(gt =0,lt=120, description="Age must be between 0 and 120")  
    #Field is used to add additional validation and metadata to the age attribute. Here, it specifies that age must be greater than 0 and less than 120 and provides a description for the field.
    email: EmailStr  
    #EmailStr is a special type provided by Pydantic for validating email addresses
    linkedIn: AnyUrl  
    #AnyUrl is a special type provided by Pydantic for validating URLs
    weight: Annotated[float , Field(gt = 0 ,strict=True)]    
    #Field is used to add additional validation and metadata to the weight attribute. Here, it specifies that weight must be greater than or equal to 0 and provides a description for the field.
    #strict = true means donot do the type conversion, if the value is not of type float, it will raise a validation error. 
    married: bool = False  #default value is False
    allergies: Annotated[Optional[list[str]] , Field(default=None, max_length=5)]  
    #list containing only string values
    #when any field is set Optional means This field can contain either a string OR None.
    contact_details: dict[str,str] 
    #dictionary containing only string values for both key and value

def insert_patient(patient: Patient):
    #function insert_patient takes an argument patient(variable) which is of type Patient
    #is patient an object of Patient class or an instance of Patient class?

    print("patient name: ", patient.name)
    print("patient age: ", patient.age)
    print("patient inserted successfully")

def update_patient(patient: Patient):
  
    print("patient name: ", patient.name)
    print("patient age: ", patient.age)
    print("patient updated successfully")

patient_info = { 'name' : "Suman", 'age' :24, 'email': 'suman@example.com', 'linkedIn': 'https://www.linkedin.com/in/suman', 'weight': 70.5,  'contact_details': {'email': 'suman@example.com', 'phone': '1234567890'}} # just a dictionary with patient information

#patient_info = { 'name' : "Suman", 'age' :24, 'weight': 70.5, 'married': False, 'allergies': ["pollen", "nuts"], 'contact_details': {'email': 'sdd@gmail.com', 'phone': 322434554} }
# the above patient_info gives Validation error because the value of 'phone' is an integer, but the model expects a string. with the help of pydantic this validation error can be handled easily 
#patient1 is object of Patine class
patient1 = Patient(**patient_info)  #why ** is being used 
#** simply takes each key-value pair and passes it as keyword arguments.** means "Open the bag and hand each item separately.
#Patient(**patient_info) is equivalent to Patient(name="Suman", age=24)
#if this is used Patient(patient_info),Python passes the entire dictionary as one positional argument.But the Patient constructor isn't expecting one unnamed dictionary argument in this context—it expects fields like name= and age= 
print("patient1 name: ", patient1.name)
print("patient.allergies: ", patient1.allergies)
print("patient.married: ", patient1.married)

insert_patient(patient1)
update_patient(patient1)