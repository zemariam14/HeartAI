from fastapi import FastAPI
from app.api import predict

app = FastAPI()

app.include_router(predict.router, prefix="/api")

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.get("/version")
def version():
    return {
        "model_version": "1.0.0",
        "api_version": "v1"
    }
