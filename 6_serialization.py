from pydantic import BaseModel
#In this we would see how can we export the pydantic model objects into python dictionary and json format. Pydantic provides us built-in methods to do this. We can use model_dump() method to export the pydantic model object into python dictionary and model_dump_json() method to export the pydantic model object into json format.

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str = "Male"
    address: Address

address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}
#unpack the dictionary into the Address model using ** operator
address1 = Address(**address_dict)
print("address1: ", address1)

print(type(address1))

patient_info = {'name': 'John Doe', 'age': 30, 'gender': 'Male', 'address': address1}


patient1 = Patient(**patient_info)
print(type(patient1))
#model_dump() converts the pydantic model object into python dictionary
temp = patient1.model_dump()
print("temp: ", temp)
print(type(temp))
#model_dump_json() converts the pydantic model object into json format
temp1 = patient1.model_dump_json()
print("temp1: ", temp1)
print(type(temp1))
# model_dump() method also allows us to include or exclude specific fields from the output dictionary. We can use include and exclude parameters to specify the fields we want to include or exclude. The include and exclude parameters accept a set of field names. If we want to include only specific fields, we can pass a set of field names to the include parameter. If we want to exclude specific fields, we can pass a set of field names to the exclude parameter.
temp2 = patient1.model_dump(include=['name', 'age'])
temp3 = patient1.model_dump(exclude=['address'])
temp4 = patient1.model_dump(exclude={'address': ['city', 'state']})
print("temp2: ", temp2) 
print("temp3: ", temp3)
print("temp4: ", temp4)

#here we are not specifying the gender field explicitly in the dictionary, so it will take the default value of "Male" as specified
patient_info2 = {'name': 'Eleven', 'age': 13, 'address': Address(city='Hawkins lab', state='America', pin='90001')}
patient2 = Patient(**patient_info2)
t = patient2.model_dump(exclude_unset=True) #exclude_unset=True will exclude the fields which are not set explicitly in the dictionary 
print("t: ", t)
