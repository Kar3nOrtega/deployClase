import pickle
from diabetes import DiabetesData
from fastapi import APIRouter
from asignatura import asignatura
from schemas import schemas
import numpy as np

router = APIRouter()

pkl_filenamec = "RFDiabetesv102.pkl"
with open(pkl_filenamec,'rb') as file:
    model = pickle.load(file)

labels = {"Sano","Posible Diabetes"}


@router.get("/")    
async def root():
    return {
        "message":"IA service"
    }

@router.post("/predict")
def predict_diabetes(data:schemas.DiabetesData):
    data = data.model_dump()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']

    xin = np.array([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]).reshape(1,8)

    prediction = model.predict(xin)
    yout = labels[prediction[0]]

    return {
    'prediction': yout
    }