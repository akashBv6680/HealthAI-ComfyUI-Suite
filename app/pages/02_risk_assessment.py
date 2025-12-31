import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    genai = None

st.set_page_config(page_title="Risk Assessment", page_icon="📄", layout="wide")
st.title("📄 Risk Assessment")
st.subheader("AI-Powered Health Risk Analysis with RAG")

if 'current_patient' not in st.session_state or st.session_state.current_patient is None:
    st.warning("⚠️ No patient selected. Go to Patient Intake first.")
else:
    patient = st.session_state.current_patient
    st.info(f"Patient: {patient['name']} (ID: {patient['patient_id']})")
    
    st.markdown("---")
    st.markdown("### Vital Signs Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("BP", f"{patient['systolic_bp']}/{patient['diastolic_bp']} mmHg")
    col2.metric("HR", f"{patient['heart_rate']} bpm")
    col3.metric("O2 Sat", f"{patient['oxygen_saturation']}%")
    col4.metric("Temp", f"{patient['temperature']}°C")
    
    st.markdown("---")
    st.markdown("### Risk Analysis")
    
    risk_score = 0
    risks = []
    
    if patient['systolic_bp'] > 140 or patient['diastolic_bp'] > 90:
        risk_score += 25
        risks.append("Hypertension risk detected")
    
    if patient['heart_rate'] > 100 or patient['heart_rate'] < 60:
        risk_score += 20
        risks.append("Abnormal heart rate")
    
    if patient['oxygen_saturation'] < 95:
        risk_score += 30
        risks.append("Low oxygen saturation")
    
    if patient['blood_glucose'] > 126 or patient['blood_glucose'] < 70:
        risk_score += 20
        risks.append("Abnormal blood glucose")
    
    if patient['temperature'] > 38 or patient['temperature'] < 36:
        risk_score += 15
        risks.append("Abnormal temperature")
    
    if "Diabetes" in patient.get('conditions', []):
        risk_score += 10
    
    if "Hypertension" in patient.get('conditions', []):
        risk_score += 10
    
    risk_score = min(risk_score, 100)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.progress(risk_score / 100)
    with col2:
        if risk_score < 30:
            st.success(f"Low Risk: {risk_score}%")
        elif risk_score < 70:
            st.warning(f"Medium Risk: {risk_score}%")
        else:
            st.error(f"High Risk: {risk_score}%")
    
    if risks:
        st.markdown("### Detected Risks")
        for risk in risks:
            st.warning(f"• {risk}")
    
    st.markdown("---")
    st.markdown("### Gemini AI Analysis")
    
    if genai and 'GEMINI_API_KEY' in st.secrets:
        if st.button("Generate AI Analysis", use_container_width=True):
            try:
                genai.configure(api_key=st.secrets['GEMINI_API_KEY'])
                model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"""Analyze this patient health data and provide brief clinical recommendations:
                Patient: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}
                BP: {patient['systolic_bp']}/{patient['diastolic_bp']}, HR: {patient['heart_rate']}, O2: {patient['oxygen_saturation']}%, Glucose: {patient['blood_glucose']}
                Conditions: {', '.join(patient.get('conditions', []))}
                Risk Score: {risk_score}%
                Provide 3-4 actionable recommendations."""
                
                response = model.generate_content(prompt)
                st.success("AI Analysis Complete")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.info("Gemini API not configured")
    
    st.markdown("---")
    st.info("📄 Next: Go to 'Visual Reports' to generate heatmaps")
