from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    sex: int              # 1 for Male, 0 for Female
    trestbps: float
    chol: float
    fbs: int              # 1 or 0
    restecg: str
    thalch: float
    exang: int            # 1 or 0
    oldpeak: float
    slope: str
    ca: float
    thal: str
    cp: str
