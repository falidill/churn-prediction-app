# 📉 Customer Churn Prediction App

This Streamlit web app predicts the probability that a customer will churn based on input features such as contract type, tenure, service usage, and more. It’s designed to help businesses identify high-risk customers and make proactive retention decisions.

🔗 **Live App**: [Try it on Streamlit Cloud](https://churn-prediction-app-jaztukg9szzayoz24bwkgk.streamlit.app/)  
📂 **Repository**: [View on GitHub](https://github.com/your-username/churn-prediction-app)

---

## 🚀 Key Features

- **Predictive Model**: XGBoost Classifier trained on a public churn dataset
- **User-Friendly Interface**: Streamlit-powered form for entering customer attributes
- **Risk Scoring**: Outputs churn probability with custom messages
- **Explainability**: SHAP integration for interpreting key risk drivers
- **Report Generator**: Optional PDF churn reports for business stakeholders *(coming soon)*

---

## 📊 Technologies Used

- Python
- Streamlit
- XGBoost
- SHAP
- Scikit-learn
- Joblib

---

## 📁 Files in This Repo

| File                  | Purpose                                                         |
|-----------------------|-----------------------------------------------------------------|
| `churn_assistant_app.py` | Streamlit app code                                            |
| `xgb_model.pkl`       | Trained XGBoost churn model                                     |
| `scaler.pkl`          | Scaler used during training (StandardScaler)                   |
| `feature_columns.pkl` | List of features in correct order used for training            |
| `requirements.txt`    | Python dependencies for Streamlit Cloud deployment             |


Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run churn_assistant_app.py

## ⚙️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/fali/churn-prediction-app.git
   cd churn-prediction-app

📬 Feedback
Feel free to open an issue or reach out on LinkedIn!
