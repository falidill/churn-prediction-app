from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", size=16)
        self.cell(0, 10, "Churn Risk Report", ln=True, align="C")
        self.ln(10)

def generate_churn_report(customer_data, churn_prob, risk_level, top_features, persona):
    pdf = PDF()
    pdf.add_page()

    # Add Unicode font
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    # Add prediction details
    pdf.cell(0, 10, f"Churn Probability: {round(churn_prob * 100, 2)}%", ln=True)
    pdf.cell(0, 10, f"Risk Level: {risk_level}", ln=True)
    pdf.cell(0, 10, f"Customer Persona: {persona}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, "Top Contributing Features:", ln=True)
    for feat in top_features:
        pdf.cell(0, 10, f"- {feat}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, "Customer Details:", ln=True)
    for key, value in customer_data.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)

    pdf.output("churn_report.pdf")
