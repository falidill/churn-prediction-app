# churn_assistant_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# --- Load trained model and scaler (from your previous churn project) ---
model = joblib.load("xgb_model.pkl")           # or rf_model.pkl / logreg_model.pkl
scaler = joblib.load("scaler.pkl")             # If you used one for numeric features
feature_columns = joblib.load("feature_columns.pkl")  # Column order used during training

# --- App Title ---
st.title("🔍 Churn Risk Assistant")
st.write("Predict customer churn and suggest actions based on risk level.")

# --- Input Form ---
with st.form("churn_form"):
    st.subheader("📋 Customer Details")

    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total_charges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    submitted = st.form_submit_button("Predict Churn")

# --- When submitted ---
if submitted:
    # Create input dataframe
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": contract,
        "PaymentMethod": payment_method,
        "InternetService": internet_service
    }
    input_df = pd.DataFrame([input_dict])

    # One-hot encode like training data
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

    # Scale numeric columns
    input_encoded_scaled = scaler.transform(input_encoded)

    # Predict
    churn_prob = model.predict_proba(input_encoded_scaled)[0][1]
    churn_percent = round(churn_prob * 100, 2)

    st.subheader("🧠 Prediction Result")
    st.write(f"**Estimated Churn Risk: {churn_percent}%**")

    if churn_prob > 0.7:
        st.error("⚠️ High Risk – Consider immediate retention outreach.")
    elif churn_prob > 0.4:
        st.warning("🟠 Medium Risk – Monitor and offer incentives.")
    else:
        st.success("✅ Low Risk – No immediate action needed.")
