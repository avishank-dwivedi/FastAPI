from pydantic import BaseModel , EmailStr ,AnyUrl , Field
from typing import List ,Dict , Optional , Annotated

class Patient(BaseModel):
    name: Annotated[str , Field(max_length=50, title='Name of the patient' ,description='Givethe name of the patient in less then 50 chars', examples=['Nitish', 'Amit'])]
    Email:EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool , Field(default=None , description='is the patient married or not')]
    allergies:Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details:Optional[Dict[str , str]]=None

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('inserted')


Patient_info = {'name':'nitish' , 'age':30 ,'Email':'dsin@gmail.com','linkedin_url':'https://@avishank733?si=rywdRwnvkE14N68z', 'weight':75.2,'married':True,'allergies':['pollen','dust'], 'contact_details':{'phone':'644844651'}}
Patient1 = Patient(**Patient_info)
insert_patient_data(Patient1)