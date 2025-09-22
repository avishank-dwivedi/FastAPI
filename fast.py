from fastapi import FastAPI , Path , HTTPException ,Query
import json
app = FastAPI()

def load_data():
    with open('Patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message' :'patient Management  System API '}

@app.get("/about")
def about():
    return {'message': 'A Fully functional API to manage your patient records'}

@app.get('/view')
@app.get('/view')

def view():
    data = load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):

    #load all the patients
    data = load_data()
    for patient in data:
        if patient["patient_id"] ==patient_id:
            return patient
    raise HTTPException(status=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of age, height, weight, or bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")
):
    # valid fields in your dataset
    valid_fields = ["age", "height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field. Select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Select between 'asc' and 'desc'")
    
    data = load_data()

    # 'reverse=True' means descending
    reverse = True if order == "desc" else False

    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=reverse)
    return sorted_data
