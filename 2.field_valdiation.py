from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    Email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('Email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls , value):
        return value.upper()



    @staticmethod
    def insert_patient_data(patient:"Patient"):
        print(patient.name)
        print(patient.age)
        print(patient.allergies)
        print(patient.married)
        print('inserted')


# Create Patient instance outside the class
Patient_info = {
    'name': 'nitish',
    'age': 30,
    'Email': 'dsin@icici.com',
    'weight': 75.2,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '644844651'}
}

Patient1 = Patient(**Patient_info)
Patient.insert_patient_data(Patient1)
