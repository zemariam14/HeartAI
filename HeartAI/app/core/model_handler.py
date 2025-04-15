import joblib
import numpy as np
from pathlib import Path
from app.core.preprocess import Preprocessor

class ModelHandler:
    def __init__(self, model_path: str = "app/models/model.pkl"):
        self.model_path = Path(model_path)
        self.model = self._load_model()
        self.preprocessor = Preprocessor()  # custom preprocessing logic

    def _load_model(self):
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        return joblib.load(self.model_path)

    def predict(self, input_dict: dict) -> float:
        # 1. Preprocess the input
        processed_input = self.preprocessor.transform(input_dict)

        # 2. Predict using the model
        prediction = self.model.predict(processed_input) 

        # 3. Return the prediction as a plain value
        return float(prediction[0])
