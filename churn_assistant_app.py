# churn_assistant_app.py
from pdf_utils import generate_churn_report

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# --- Load trained model and scaler ---
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# --- App Title ---
st.title("\U0001F50D Churn Risk Assistant")
st.write("Predict customer churn, assign a persona, and generate a downloadable report.")

# --- Input Form ---
with st.form("churn_form"):
    st.subheader("\U0001F4CB Customer Details")

    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total_charges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    submitted = st.form_submit_button("Predict Churn")

# --- When submitted ---
if submitted:
    input_dict = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Contract": contract,
        "PaymentMethod": payment_method,
        "InternetService": internet_service
    }
    input_df = pd.DataFrame([input_dict])

    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)
    input_encoded_scaled = scaler.transform(input_encoded)

    churn_prob = model.predict_proba(input_encoded_scaled)[0][1]
    churn_percent = round(churn_prob * 100, 2)

    st.subheader("\U0001F9E0 Prediction Result")
    st.write(f"**Estimated Churn Risk: {churn_percent}%**")

    # Risk level
    if churn_prob > 0.8:
        risk_level = "\U0001F534 High Risk"
        st.error("⚠️ High Risk – Consider immediate retention outreach.")
        persona = {
            "name": "The Deal Seeker",
            "description": "Loyal but budget-sensitive, often motivated by discounts, better contracts, or perks. May churn if not engaged with retention offers."
        }
    elif churn_prob > 0.5:
        risk_level = "\U0001F7E1 Medium Risk"
        st.warning("🟠 Medium Risk – Monitor and offer incentives.")
        persona = {
            "name": "The Fence Sitter",
            "description": "Undecided and easily swayed by service experience. Needs consistent engagement and reassurance to remain loyal."
        }
    else:
        risk_level = "\U0001F7E2 Low Risk"
        st.success("✅ Low Risk – No immediate action needed.")
        persona = {
            "name": "The Loyalist",
            "description": "Stable and satisfied with the current service. Unlikely to churn unless there’s a major disruption."
        }

    customer_data = {
        "Tenure": tenure,
        "Contract": contract,
        "Payment Method": payment_method,
        "Internet Service": internet_service,
        "Monthly Charges": monthly_charges,
        "Total Charges": total_charges
    }

    top_features = ["Contract Type", "Tenure", "Monthly Charges"]  # Placeholder

    generate_churn_report(customer_data, churn_prob, risk_level, top_features, persona)

    with open("churn_report.pdf", "rb") as file:
        st.download_button(
            label="\U0001F4C4 Download Churn Report",
            data=file,
            file_name="churn_report.pdf",
            mime="application/pdf"
        )
