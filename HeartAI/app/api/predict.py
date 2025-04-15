from fastapi import APIRouter, HTTPException
from app.schemas.input import InputData
from app.core.model_handler import ModelHandler

router = APIRouter()
model_handler = ModelHandler()

@router.post("/predict")
async def get_prediction(input_data: InputData):
    try:
        prediction = model_handler.predict(input_data.dict())
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


