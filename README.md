🚀 Loan Default Prediction (Binary Classification)

Built an end-to-end machine learning system to predict whether a borrower will default or repay a loan using financial and credit history features.

📊 Model Performance

Best Model: XGBoost

Test ROC-AUC: 0.95

Accuracy: ~93.5%

Optimized decision threshold to 0.4 for better defaulter detection.

🧠 Key Features Used

person_income (annual)

loan_amnt

loan_percent_income

loan_grade

past default history

credit history length

employment length

home ownership

loan intent

⚙️ Techniques Applied

Outlier handling

Feature engineering (loan_percent_income, is_high_debt)

ColumnTransformer (OneHot + Ordinal encoding + Scaling)

Pipeline integration

Model comparison (Logistic, Random Forest, XGBoost)

Hyperparameter tuning using GridSearchCV

Threshold optimization

Model serialization using joblib

🛠 Tech Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost, Joblib

🎯 Outcome

Developed a production-ready credit risk model with strong class separation (AUC ≈ 0.95), suitable for deployment in loan approval systems.