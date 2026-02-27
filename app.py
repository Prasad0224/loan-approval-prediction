import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Loan Risk Scoring",
    layout="centered"
)

st.title("🏦 Loan Risk Scoring System")
st.write("Enter applicant details to predict loan approval status.")

with st.form("loan_form"):

    person_income = st.number_input("Annual Income (INR)")
    loan_amnt = st.number_input("Loan Amount")
    loan_int_rate = st.number_input("Interest Rate (%)")

    cb_person_cred_hist_length = st.number_input(
        "Credit History Length (years)"
    )

    person_emp_length = st.number_input(
        "Employment Length (years)"
    )

    person_age = st.number_input("Age")

    cb_person_default_on_file = st.selectbox(
        "Previous Default on File?",
        ["Y", "N"]
    )

    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

    person_home_ownership = st.selectbox(
        "Home Ownership",
        ["RENT", "OWN", "MORTGAGE", "OTHER"]
    )

    loan_intent = st.selectbox(
        "Loan Purpose",
        [
            "PERSONAL",
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "HOMEIMPROVEMENT",
            "DEBTCONSOLIDATION"
        ]
    )

    submit = st.form_submit_button("Predict")

if submit:
    payload = {
        "person_income": person_income,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "cb_person_cred_hist_length": cb_person_cred_hist_length,
        "person_emp_length": person_emp_length,
        "person_age": person_age,
        "cb_person_default_on_file": cb_person_default_on_file,
        "loan_grade": loan_grade,
        "person_home_ownership": person_home_ownership,
        "loan_intent": loan_intent
    }

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()

        decision = result["decision"]
        prob = result["default_probability"]

        if decision == "Approve":
            st.success(f"Decision: **{decision}**")
            st.info(f"Default Probability: **{prob}**")
        else:
            st.error(f"Decision: **{decision}**")
            st.info(f"Default Probability: **{prob}**")

    else:
        st.error("Prediction failed. Check backend or input values.")