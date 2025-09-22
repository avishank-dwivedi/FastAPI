from pydantic import BaseModel

class Address(BaseModel):

    city : str
    state: str
    pin: str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

Address_dict = { 'city':'gurgram' , 'state': 'haryana', 'pin':'252524'}
Address1 = Address(**Address_dict)

Patient_dict = {'name':'nitish' , 'gender':'male', 'age':51 , 'address':Address_dict}

patient1 = Patient(**Patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)