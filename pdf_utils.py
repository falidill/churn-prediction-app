from fpdf import FPDF

# --- Generate PDF Report Function ---
def generate_churn_report(customer_data, churn_prob, risk_level, top_features, persona):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Customer Churn Report", ln=True, align='C')

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Customer Information:", ln=True)
    pdf.set_font("Arial", size=11)
    for key, value in customer_data.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Prediction Summary:", ln=True)
    pdf.set_font("Arial", size=11)
    churn_percent = round(churn_prob * 100, 2)
    risk_level_clean = risk_level.replace("🔴", "High").replace("🟡", "Medium").replace("🟢", "Low")
    pdf.cell(0, 10, f"Predicted Churn Probability: {churn_percent}%", ln=True)
    pdf.cell(0, 10, f"Risk Level: {risk_level_clean}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Top Influencing Factors:", ln=True)
    pdf.set_font("Arial", size=11)
    for feat in top_features:
        pdf.cell(0, 10, f"- {feat}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Customer Persona:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, f"{persona['name']}: {persona['description']}")

    # Save the report
    pdf.output("churn_report.pdf")
