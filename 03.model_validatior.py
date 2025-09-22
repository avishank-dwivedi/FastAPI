from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    Email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode ='after')
    def validate_emergency_contact(cls , model):
        if model.age > 60 and 'emergency'  not in model.contact_details:
            raise ValueError('Patients older then 60 must have an emergency contact')
        return model

    @staticmethod
    def insert_patient_data(patient:"Patient"):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('inserted')



Patient_info = {
    'name': 'nitish',
    'age': 59,
    'Email': 'dsin@icici.com',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '644844651','emergency':'84684658'}
}

Patient1 = Patient(**Patient_info)
Patient.insert_patient_data(Patient1)