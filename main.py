from fastapi import FastAPI
from schema.user_input import LoanApplicant
from models.predict import predict_loan


app = FastAPI(title="Loan Default Prediction API")


@app.get("/")
def home():
    return {"status": "API is running"}

@app.get("/health")
def healthcheck():

    return {
        "status": "ok",
        "service": "loan-risk-scoring",
        "model_loaded": True
    }


@app.post("/predict")
def predict(applicant: LoanApplicant):
    return predict_loan(applicant)
