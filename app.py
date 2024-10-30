import streamlit as st

# Sample risk calculation functions (implement logic per guidelines)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    if smoker and systolic_bp > 140:
        return "High"
    return "Moderate"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    if fasting_glucose > 126 or hba1c > 6.5:
        return "High"
    return "Moderate"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    if smoking_years > 20 and exacerbations_last_year > 2:
        return "High"
    return "Moderate"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    if frequency_of_symptoms > 4 or nighttime_symptoms > 2:
        return "High"
    return "Moderate"

# AI Assistant Function with Detailed Guideline-Based Recommendations
def ai_assistant_response(query, results):
    responses = []
    for condition, risk in results.items():
        if condition == "Cardiovascular":
            if risk == "High":
                responses.append(
                    "### Cardiovascular Risk - High Level\n"
                    "- **Lifestyle Changes**: Adopt the DASH diet, reduce sodium, increase fruits, vegetables, whole grains.\n"
                    "- **Medications**: Initiate antihypertensives (e.g., ACE inhibitors), high-intensity statins per AHA/ACC guidelines.\n"
                    "- **Follow-Up**: Reassess blood pressure, lipids every 3 months.\n"
                    "- **Resources**: [AHA Guidelines](https://www.heart.org/en/professional/quality-improvement/aha-quality-improvement-guidelines)"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Cardiovascular Risk - Moderate Level\n"
                    "- **Lifestyle**: Balanced diet, reduce processed foods, increase activity.\n"
                    "- **Medications**: Moderate-intensity statins if needed, monitor blood pressure closely.\n"
                    "- **Follow-Up**: Follow-ups every 6-12 months.\n"
                )
            else:
                responses.append("### Cardiovascular Risk - Low Level\nRoutine check-ups recommended annually.\n")

        elif condition == "Diabetes":
            if risk == "High":
                responses.append(
                    "### Diabetes Risk - High Level\n"
                    "- **Lifestyle Changes**: Low-carb, high-fiber diet; 150 mins exercise weekly.\n"
                    "- **Medications**: Start metformin, consider SGLT-2 inhibitors/GLP-1 as per ADA.\n"
                    "- **Monitoring**: HbA1c every 3 months.\n"
                    "- **Resources**: [ADA Standards of Medical Care](https://www.diabetes.org/clinical-resources/standards-of-care)"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Diabetes Risk - Moderate Level\n"
                    "- **Diet & Exercise**: Mediterranean or DASH diet, 150 mins activity weekly.\n"
                    "- **Monitoring**: HbA1c every 6 months.\n"
                )
            else:
                responses.append("### Diabetes Risk - Low Level\nRoutine annual fasting glucose check recommended.\n")

        elif condition == "COPD":
            if risk == "High":
                responses.append(
                    "### COPD Risk - High Level\n"
                    "- **Smoking Cessation**: Immediate cessation, pharmacotherapy as needed.\n"
                    "- **Medications**: LABA or LAMA, inhaled corticosteroids for frequent exacerbators.\n"
                    "- **Pulmonary Rehab**: For improved respiratory function.\n"
                    "- **Follow-Up**: Lung function every 3 months.\n"
                    "- **Resources**: [GOLD Guidelines](https://goldcopd.org/gold-reports/)"
                )
            elif risk == "Moderate":
                responses.append(
                    "### COPD Risk - Moderate Level\n"
                    "- **Avoid Pollutants**: Limit exposure to irritants.\n"
                    "- **Medications**: Short-acting bronchodilators as needed.\n"
                    "- **Follow-Up**: Annual pulmonary function test.\n"
                )
            else:
                responses.append("### COPD Risk - Low Level\nAvoid smoking, occupational hazards; annual flu vaccine recommended.\n")

        elif condition == "Asthma":
            if risk == "High":
                responses.append(
                    "### Asthma Risk - High Level\n"
                    "- **Medications**: Inhaled corticosteroids, long-acting beta-agonists.\n"
                    "- **Action Plan**: Personalized asthma action plan.\n"
                    "- **Follow-Up**: Monthly visits until stable.\n"
                    "- **Resources**: [GINA Guidelines](https://ginasthma.org/gina-reports/)"
                )
            elif risk == "Moderate":
                responses.append(
                    "### Asthma Risk - Moderate Level\n"
                    "- **Medications**: Inhaled corticosteroids, evaluate long-acting bronchodilator.\n"
                    "- **Follow-Up**: Every 3-6 months.\n"
                )
            else:
                responses.append("### Asthma Risk - Low Level\nAnnual check-ups to monitor lung function.\n")
    return "\n\n".join(responses)

# Initialize Streamlit app
st.title("Chronic Care Management Tool")
st.write("This application helps assess risks for various chronic conditions and provides personalized care plans.")

# Initialize session state for results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Risk Assessment Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=120, value=50, key="age")
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=80, max_value=200, value=120, key="systolic_bp")
    cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=150, max_value=300, value=200, key="cholesterol")
    smoker = st.checkbox("Smoker", key="smoker")

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker, cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, key="bmi_diabetes")
    age_diabetes = st.number_input("Age", min_value=18, max_value=100, value=30, key="age_diabetes")
    family_history = st.checkbox("Family History of Diabetes", key="family_history")
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=100, key="fasting_glucose")
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.0, key="hba1c")

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age_diabetes, family_history, fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years Smoking", min_value=0, max_value=50, value=10, key="smoking_years")
    age_copd = st.number_input("Age", min_value=18, max_value=100, value=30, key="age_copd")
    fev1 = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=80, key="fev1")
    exacerbations_last_year = st.number_input("Exacerbations Last Year", min_value=0, max_value=10, value=1, key="exacerbations_last_year")

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age_copd, fev1, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Symptoms (0-7 days/week)", 0, 7, 2)
    nighttime_symptoms = st.slider("Nighttime Symptoms (0-7 days/week)", 0, 7, 1)
    inhaler_use = st.checkbox("Regular Inhaler Use")
    fev1_asthma = st.number_input("FEV1 (%)", min_value=20, max_value=100, value=85, key="fev1_asthma")
    eosinophil_count = st.number_input("Eosinophil Count (cells/mcL)", min_value=0, max_value=500, value=200)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

# Unified Care Plan Tab
with tab5:
    st.header("Personalized Unified Care Plan")
    if st.button("Generate Unified Care Plan"):
        unified_plan = ai_assistant_response("Generate care plan", st.session_state['results'])
        st.write(unified_plan)
