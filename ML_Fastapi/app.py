from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal, Annotated
from fastapi.responses import JSONResponse
import joblib
import pandas as pd

# Load the model
with open('model.pkl', 'rb') as f:
    model = joblib.load("model.joblib")

app = FastAPI()

# Define city tiers
tier_1_cities = {"city1", "city2", "city3"}  # Replace with actual city names
tier_2_cities = {"city4", "city5", "city6"}  # Replace with actual city names

# Pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user')]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description='Height of the user')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual Salary of the user')]
    smoker: Annotated[bool, Field(..., description='Is the user a smoker')]
    city: Annotated[str, Field(..., description='The city that the user belongs to')]
    occupation: Annotated[
        Literal['retired', 'freelancer', 'student', 'government_job',
                'business_owner', 'unemployed', 'private_job'],
        Field(..., description='Occupation of the user')
    ]

    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)

    @property
    def lifecycle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"

    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:  # Fixed typo here
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

@app.post('/predict')
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifecycle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'predicted_category': prediction})