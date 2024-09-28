from pydantic import BaseModel

class DiabetesData(BaseModel):
    Pregnacies: int
    Glucose: int
    BloodPressure: int
    SkinThickness : int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: int
    Age: int
   