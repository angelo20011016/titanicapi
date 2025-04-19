from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# 載入模型
model = joblib.load('model/titanic_model.pkl')

# 輸入格式定義
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int
    FamilySize: int
    IsAlone: int
    Title: int

@app.post("/predict")
def predict_survival(data: Passenger):
    input_data = np.array([[data.Pclass, data.Sex, data.Age, data.SibSp,
                            data.Parch, data.Fare, data.Embarked,
                            data.FamilySize, data.IsAlone, data.Title]])
    pred = model.predict(input_data)
    return {"Survived": int(pred[0])}
