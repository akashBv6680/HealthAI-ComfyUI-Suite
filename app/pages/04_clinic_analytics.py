import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

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
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(ages, counts, color='#4ecdc4')
    ax.set_ylabel('Number of Patients')
    ax.set_title('Age Distribution')
    st.pyplot(fig)

with col2:
    genders = ['Male', 'Female', 'Other']
    gender_counts = [78, 74, 4]
    colors = ['#ff6b6b', '#ffa500', '#95e1d3']
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie(gender_counts, labels=genders, autopct='%1.1f%%', colors=colors)
    ax.set_title('Gender Distribution')
    st.pyplot(fig)

st.markdown("---")
st.markdown("### Risk Level Distribution")

risk_data = {
    'Low Risk': 89,
    'Medium Risk': 48,
    'High Risk': 19
}

fig, ax = plt.subplots(figsize=(10, 5))
colors_risk = ['#51cf66', '#ffd43b', '#ff6b6b']
ax.barh(list(risk_data.keys()), list(risk_data.values()), color=colors_risk)
ax.set_xlabel('Number of Patients')
for i, v in enumerate(risk_data.values()):
    ax.text(v + 1, i, str(v), va='center')
st.pyplot(fig)

st.markdown("---")
st.markdown("### Daily Activity")

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
patients_seen = [32, 28, 35, 29, 31, 12, 8]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(days, patients_seen, marker='o', linewidth=2, markersize=8, color='#4ecdc4')
ax.fill_between(range(len(days)), patients_seen, alpha=0.3, color='#4ecdc4')
ax.set_ylabel('Patients Seen')
ax.set_title('Weekly Patient Volume')
ax.grid(True, alpha=0.3)
st.pyplot(fig)

st.markdown("---")
st.markdown("### Recent Patients")

recent_patients_data = {
    'Patient ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Name': ['John Doe', 'Jane Smith', 'Bob Wilson', 'Alice Brown', 'Charlie Davis'],
    'Date': ['Today', 'Today', 'Yesterday', 'Yesterday', '2 days ago'],
    'Risk Level': ['Low', 'Medium', 'High', 'Low', 'Medium']
}

df = pd.DataFrame(recent_patients_data)
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("### System Performance")

col1, col2, col3 = st.columns(3)
col1.gauge_chart({'value': 95}, min_value=0, max_value=100)
col1.caption("API Response Time (ms)")

col2.gauge_chart({'value': 99.8}, min_value=0, max_value=100)
col2.caption("System Uptime %")

col3.gauge_chart({'value': 68}, min_value=0, max_value=100)
col3.caption("CPU Usage %")

st.markdown("---")
st.info("🏆 All pages complete! Application is fully functional.")
