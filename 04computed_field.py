from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict
class Patient(BaseModel):
    name: str
    Email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round((self.weight)/(self.height**2),2)
        return bmi

    @staticmethod
    def insert_patient_data(patient:"Patient"):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('BMI' , patient.bmi)
        print('inserted')


Patient_info = {
    'name': 'nitish',
    'age': 54,
    'Email': 'dsin@icici.com',
    'weight': 75.2,
    'height' :1.75,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '644844651','emergency':'84684658'}
}

Patient1 = Patient(**Patient_info)
Patient.insert_patient_data(Patient1)