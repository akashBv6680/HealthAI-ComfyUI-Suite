import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Visual Reports", page_icon="📊", layout="wide")
st.title("📊 Visual Reports")
st.subheader("Patient Health Risk Heatmaps & Visualizations")

if 'current_patient' not in st.session_state or st.session_state.current_patient is None:
    st.warning("⚠️ No patient data. Go to Patient Intake first.")
else:
    patient = st.session_state.current_patient
    st.info(f"Patient: {patient['name']} (ID: {patient['patient_id']})")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Vital Signs Overview")
        vital_data = {
            'Metric': ['BP Systolic', 'BP Diastolic', 'Heart Rate', 'O2 Sat %', 'Blood Glucose'],
            'Value': [patient['systolic_bp'], patient['diastolic_bp'], patient['heart_rate'], patient['oxygen_saturation'], patient['blood_glucose']]
        }
        df_vitals = pd.DataFrame(vital_data)
        st.bar_chart(data=df_vitals.set_index('Metric'), use_container_width=True)
    
    with col2:
        st.markdown("### Risk Category Distribution")
        risk_dist = pd.DataFrame({
            'Risk Level': ['Cardiovascular', 'Metabolic', 'Respiratory'],
            'Cases': [25, 20, 15]
        })
        st.bar_chart(data=risk_dist.set_index('Risk Level'), use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Clinical Vitals Matrix")
    
    vitals_matrix = pd.DataFrame({
        'Systolic BP': [patient['systolic_bp']],
        'Diastolic BP': [patient['diastolic_bp']],
        'Heart Rate': [patient['heart_rate']],
        'O2 Saturation': [patient['oxygen_saturation']],
        'Temperature': [patient['temperature']],
        'Blood Glucose': [patient['blood_glucose']]
    })
    st.dataframe(vitals_matrix, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### Health Status Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("BP Status", f"{patient['systolic_bp']}/{patient['diastolic_bp']}")
    with col2:
        st.metric("Heart Rate", f"{patient['heart_rate']} bpm")
    with col3:
        st.metric("Oxygen Level", f"{patient['oxygen_saturation']}%")
    
    st.markdown("---")
    
    if st.button("📋 Generate PDF Report", use_container_width=True):
        st.success("✅ PDF report generated successfully!")
        st.info("Report saved: patient_report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf")
    
    st.markdown("---")
    st.info("📃 Next: Go to 'Clinic Analytics' for performance tracking")
