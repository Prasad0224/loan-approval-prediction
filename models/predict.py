import joblib
import pandas as pd

MODEL_PATH = "models/loan_default_model.pkl"
THRESHOLD = 0.4

model = joblib.load(MODEL_PATH)

def predict_loan(applicant):

    data = applicant.model_dump()

    df = pd.DataFrame([data])

    prob = model.predict_proba(df)[0, 1]
    decision = "Reject" if prob > THRESHOLD else "Approve"

    return {
        "default_probability": round(float(prob), 4),
        "decision": decision
    }