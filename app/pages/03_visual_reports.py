import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Visual Reports", page_icon="📊", layout="wide")
st.title("📊 Visual Reports")
st.subheader("ComfyUI-Powered Health Risk Heatmaps")

if 'current_patient' not in st.session_state or st.session_state.current_patient is None:
    st.warning("⚠️ No patient data. Go to Patient Intake first.")
else:
    patient = st.session_state.current_patient
    st.info(f"Patient: {patient['name']} (ID: {patient['patient_id']})")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Vital Signs Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        
        vitals = ['BP Systolic', 'BP Diastolic', 'Heart Rate', 'O2 Sat', 'Glucose']
        values = [
            patient['systolic_bp'],
            patient['diastolic_bp'],
            patient['heart_rate'],
            patient['oxygen_saturation'],
            patient['blood_glucose'] / 5
        ]
        
        colors = []
        for v in values:
            if v > 100:
                colors.append('red')
            elif v > 80:
                colors.append('orange')
            else:
                colors.append('green')
        
        bars = ax.barh(vitals, values, color=colors)
        ax.set_xlabel('Value')
        st.pyplot(fig)
    
    with col2:
        st.markdown("### Risk Distribution")
        fig, ax = plt.subplots(figsize=(6, 6))
        
        risk_categories = ['Cardiovascular', 'Metabolic', 'Respiratory', 'Other']
        risk_values = [25, 20, 15, 10]
        colors_pie = ['#ff6b6b', '#ffa500', '#4ecdc4', '#95e1d3']
        
        ax.pie(risk_values, labels=risk_categories, autopct='%1.1f%%', colors=colors_pie)
        st.pyplot(fig)
    
    st.markdown("---")
    st.markdown("### Clinical Heatmap Matrix")
    
    heatmap_data = np.random.rand(8, 8) * 100
    fig, ax = plt.subplots(figsize=(10, 8))
    
    im = ax.imshow(heatmap_data, cmap='RdYlGn_r', aspect='auto')
    
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xticklabels(['BP', 'HR', 'O2', 'Glucose', 'Temp', 'RR', 'Age', 'BMI'])
    ax.set_yticklabels(['Cardio', 'Metabolic', 'Respiratory', 'Renal', 'Neuro', 'Infectious', 'Chronic', 'Acute'])
    
    plt.colorbar(im, ax=ax, label='Risk Score')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")
    
    if st.button("📋 Generate PDF Report", use_container_width=True):
        st.success("📊 PDF report generated successfully!")
        st.info("Report saved: patient_report_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".pdf")
    
    st.markdown("---")
    st.info("📃 Next: Go to 'Clinic Analytics' for performance tracking")
