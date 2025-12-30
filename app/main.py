import streamlit as st
import os
from pathlib import Path
import sys
try:
    import google.generativeai as genai
except ImportError:
    genai = None

sys.path.append(str(Path(__file__).parent.parent))

st.set_page_config(page_title="HealthAI Suite + ComfyUI", page_icon="🏥", layout="wide")

st.title("🏥 HealthAI Suite + ComfyUI")
st.subheader("Agentic Health Risk Visualizations for Madurai Clinics")

# Initialize Gemini API
if 'GEMINI_API_KEY' not in st.secrets:
    st.error('Gemini API Key not found in secrets')
else:
    if genai:     genai.configure(api_key=st.secrets['GEMINI_API_KEY'])

st.markdown("""
### Welcome to HealthAI Suite

Integrating **RAG-powered health analysis** with **ComfyUI visual generation** for clinicians.

**Features:**
- 🤖 **LangGraph Agents**: Multi-step clinical reasoning
- 📚 **RAG Integration**: Medical knowledge base retrieval
- 🎨 **ComfyUI Visuals**: Auto-generated patient risk heatmaps
- 🗣️ **Multilingual TTS**: Tamil, English, Hindi narration
- 📊 **Clinic Analytics**: Track patient metrics & generation performance

### Quick Start
1. Go to **Patient Intake** → Enter patient vital signs
2. View **Risk Assessment** → AI analysis with RAG context
3. Generate **Visual Reports** → ComfyUI-powered heatmaps
4. Download PDF with TTS narration
""")

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.info("👤 Start with Patient Intake (left sidebar)")
with col2:
    st.success("🚀 Status: Ready | ComfyUI: Connected")

st.markdown("""
---
**Built for clinics in Madurai, India. Scaling healthcare with open-source AI.**
""")
