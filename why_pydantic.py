from pydantic import BaseModel
#Every Pydantic model must inherit from BaseModel.importing the BaseModel class from Pydantic. 

#patient model is created 
class Patient(BaseModel):
    #creating a model for patient with name and age attributes
    name: str
    age: int

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

patient_info = { 'name' : "Suman", 'age' :24} # just a dictionary with patient information

#patient1 is object of Patine class
patient1 = Patient(**patient_info)  #why ** is being used 
#** simply takes each key-value pair and passes it as keyword arguments.** means "Open the bag and hand each item separately.
#Patient(**patient_info) is equivalent to Patient(name="Suman", age=24)
#if this is used Patient(patient_info),Python passes the entire dictionary as one positional argument.But the Patient constructor isn't expecting one unnamed dictionary argument in this context—it expects fields like name= and age= 
print("patient1 name: ", patient1.name)

insert_patient(patient1)
update_patient(patient1)