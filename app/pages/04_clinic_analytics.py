import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Clinic Analytics", page_icon="📝", layout="wide")
st.title("📝 Clinic Analytics")
st.subheader("Track Patient Metrics & System Performance")

st.markdown("---")
st.markdown("### Key Metrics")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", "156", "+12")
col2.metric("Avg Risk Score", "42.5%", "-2.3%")
col3.metric("Reports Generated", "234", "+18")
col4.metric("System Uptime", "99.8%", "✅")

st.markdown("---")
st.markdown("### Patient Demographics")

col1, col2 = st.columns(2)

with col1:
    ages = ['0-20', '20-40', '40-60', '60-80', '80+']
    counts = [12, 45, 58, 35, 6]
    age_df = pd.DataFrame({'Age Group': ages, 'Count': counts})
    st.bar_chart(data=age_df.set_index('Age Group'), use_container_width=True)

with col2:
    genders = ['Male', 'Female', 'Other']
    gender_counts = [78, 74, 4]
    gender_df = pd.DataFrame({'Gender': genders, 'Count': gender_counts})
    st.bar_chart(data=gender_df.set_index('Gender'), use_container_width=True)

st.markdown("---")
st.markdown("### Risk Level Distribution")

risk_data = {
    'Risk Level': ['Low Risk', 'Medium Risk', 'High Risk'],
    'Patients': [89, 48, 19]
}
df_risk = pd.DataFrame(risk_data)
st.bar_chart(data=df_risk.set_index('Risk Level'), use_container_width=True)

st.markdown("---")
st.markdown("### Daily Activity")

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
patients_seen = [32, 28, 35, 29, 31, 12, 8]
activity_df = pd.DataFrame({'Day': days, 'Patients Seen': patients_seen})
st.line_chart(data=activity_df.set_index('Day'), use_container_width=True)

st.markdown("---")
st.markdown("### Recent Patients")

recent_patients_data = {
    'Patient ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Name': ['John Doe', 'Jane Smith', 'Bob Wilson', 'Alice Brown', 'Charlie Davis'],
    'Date': ['Today', 'Today', 'Yesterday', 'Yesterday', '2 days ago'],
    'Risk Level': ['Low', 'Medium', 'High', 'Low', 'Medium']
}

df_recent = pd.DataFrame(recent_patients_data)
st.dataframe(df_recent, use_container_width=True)

st.markdown("---")
st.markdown("### System Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("API Response Time", "95 ms", "-5 ms")
with col2:
    st.metric("System Uptime", "99.8%", "+0.1%")
with col3:
    st.metric("CPU Usage", "68%", "-2%")

st.markdown("---")
st.success("🏆 All analytics updated successfully!")
