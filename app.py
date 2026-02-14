from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


model = joblib.load("models/loan_default_model.pkl")
THRESHOLD = 0.4


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    income = float(data["person_income"])
    loan = float(data["loan_amnt"])

    # engineered features (same as notebook)
    loan_percent_income = loan / income
    is_high_debt = int(loan_percent_income > 0.4)

    df = pd.DataFrame([{
        "person_income": income,
        "loan_amnt": loan,
        "loan_percent_income": loan_percent_income,
        "loan_int_rate": float(data["loan_int_rate"]),
        "loan_grade": data["loan_grade"],
        "cb_person_default_on_file": data["cb_person_default_on_file"],
        "cb_person_cred_hist_length": float(data["cb_person_cred_hist_length"]),
        "person_emp_length": float(data["person_emp_length"]),
        "person_home_ownership": data["person_home_ownership"],
        "loan_intent": data["loan_intent"],
        "person_age": float(data["person_age"]),
        "is_high_debt": is_high_debt
    }])

    prob = model.predict_proba(df)[0][1]
    pred = int(prob > THRESHOLD)

    return jsonify({
        "probability": round(float(prob), 4),
        "percent": int(prob * 100),
        "decision": "Reject ❌" if pred else "Approve ✅"
    })


if __name__ == "__main__":
    app.run(debug=True)
