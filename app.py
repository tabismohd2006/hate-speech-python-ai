from fastapi import FastAPI
from pydantic import BaseModel
from model.bert_model_sentiment import predict_text

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "Python AI Server Running"
    }

@app.post("/predict")
def predict(data: TextInput):

    result = predict_text(data.text)

    return {
        "prediction": result["prediction"],
        "confidence": round(result["confidence"] * 100, 2),
        "text": result["text"]
    }