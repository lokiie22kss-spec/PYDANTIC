from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}
#unpack the dictionary into the Address model using ** operator
address1 = Address(**address_dict)
print("address1: ", address1)

print(type(address1))

patient_info = {'name': 'John Doe', 'age': 30, 'gender': 'Male', 'address': address1}

patient1 = Patient(**patient_info)
print("patient1: ", patient1)
print(type(patient1))
print("patient1.address: ", patient1.address)
print("patient1.address.city: ", patient1.address.city)

