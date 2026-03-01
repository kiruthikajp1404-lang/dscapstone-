from fastapi import FastAPI
import mlflow.sklearn
import pandas as pd
import os
#books_df = pd.read_csv("feminist_books.csv")
app = FastAPI()

# Set MLflow tracking to local folder
mlflow.set_tracking_uri("file:./mlruns")
# Load model using local path (IMPORTANT)
model = mlflow.sklearn.load_model("model")
@app.get("/")
def home():
    return {"message": "Goodreads Prediction API Running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    
    return {"prediction": prediction.tolist()}
#model = mlflow.sklearn.load_model("mlruns/models/m-ab9f111868764bf99a134689eac4e98")
#mlflow.sklearn.save_model(model, "model")

# To run the API, use the command: uvicorn app:app --reload
#CONNECTION TO THE FRONTEND
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
