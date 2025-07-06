from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Customer Churn Risk Report", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

def generate_churn_report(customer_data, churn_prob, risk_level, top_features, persona):
    pdf = PDF()
    pdf.add_page()

    # --- Customer Info ---
    pdf.section_title("Customer Overview")
    for key, value in customer_data.items():
        pdf.section_body(f"{key}: {value}")

    # --- Churn Risk ---
    pdf.section_title("Churn Risk Prediction")
    pdf.section_body(f"Estimated Probability of Churn: {round(churn_prob * 100, 2)}%")
    pdf.section_body(f"Risk Level: {risk_level}")

    # --- Top Features ---
    pdf.section_title("Key Factors Influencing Risk")
    for feature in top_features:
        pdf.section_body(f"- {feature}")

    # --- Persona ---
    pdf.section_title("Customer Persona")
    pdf.section_body(f"Persona: {persona['name']}")
    pdf.section_body(f"Description: {persona['description']}")

    # --- Save File ---
    pdf.output("churn_report.pdf")
