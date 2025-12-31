import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Patient Intake", page_icon="👤", layout="wide")
st.title("👤 Patient Intake")
st.subheader("Enter Patient Vital Signs")

if 'patients' not in st.session_state:
    st.session_state.patients = []

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Patient Information")
    patient_id = st.text_input("Patient ID", placeholder="P001")
    patient_name = st.text_input("Patient Name", placeholder="John Doe")
    age = st.number_input("Age", min_value=0, max_value=150, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

with col2:
    st.markdown("### Vital Signs")
    systolic = st.number_input("Systolic BP (mmHg)", min_value=50, max_value=250, value=120)
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=30, max_value=150, value=80)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=72)
    temperature = st.number_input("Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0, step=0.1)

st.markdown("---")

respiratory_rate = st.number_input("Respiratory Rate", min_value=8, max_value=60, value=16)
oxygen_saturation = st.number_input("Oxygen Saturation (%)", min_value=50, max_value=100, value=98)
blood_glucose = st.number_input("Blood Glucose (mg/dL)", min_value=40, max_value=500, value=100)

st.markdown("---")
st.markdown("### Medical History")
conditions = st.multiselect("Existing conditions:", ["Hypertension", "Diabetes", "Asthma", "Heart Disease", "None"])
medications = st.text_area("Medications", placeholder="List medications")

if st.button("✅ Save Patient", use_container_width=True):
    patient_data = {
        "patient_id": patient_id,
        "name": patient_name,
        "age": age,
        "gender": gender,
        "systolic_bp": systolic,
        "diastolic_bp": diastolic,
        "heart_rate": heart_rate,
        "temperature": temperature,
        "respiratory_rate": respiratory_rate,
        "oxygen_saturation": oxygen_saturation,
        "blood_glucose": blood_glucose,
        "conditions": conditions,
        "medications": medications,
        "timestamp": datetime.now().isoformat()
    }
    st.session_state.patients.append(patient_data)
    st.success(f"✅ Saved: {patient_name}")
    st.json(patient_data)

if st.session_state.patients:
    st.markdown("### Patients")
    patient_df = pd.DataFrame([{"ID": p["patient_id"], "Name": p["name"], "Age": p["age"], "HR": p["heart_rate"], "BP": f"{p['systolic_bp']}/{p['diastolic_bp']}"} for p in st.session_state.patients])
    st.dataframe(patient_df, use_container_width=True)
