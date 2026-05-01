import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG (DARK STYLE)
# -----------------------------
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (DARK UI)
# -----------------------------
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("models/fraud_model.pkl")

# -----------------------------
# TITLE
# -----------------------------
st.title("💳 AI Fraud Detection Dashboard")

# -----------------------------
# SIDEBAR INPUT
# -----------------------------
st.sidebar.header("Transaction Input")

amount = st.sidebar.slider("Amount", 1, 5000, 500)
hour = st.sidebar.slider("Hour of Transaction", 0, 23, 12)

# -----------------------------
# PREDICTION
# -----------------------------
if st.sidebar.button("Analyze Transaction"):

    cols = ['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
            'V11','V12','V13','V14','V15','V16','V17','V18',
            'V19','V20','V21','V22','V23','V24','V25','V26',
            'V27','V28','Amount']

    values = list(np.random.normal(0, 1, 28)) + [amount]

    data = pd.DataFrame([values], columns=cols)

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Amount", f"₹{amount}")
    col2.metric("⏰ Hour", hour)
    col3.metric("⚠️ Fraud Probability", f"{prob*100:.2f}%")

    # -----------------------------
    # RESULT ALERT
    # -----------------------------
    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

    # -----------------------------
    # GAUGE CHART (PREMIUM)
    # -----------------------------
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob*100,
        title={'text': "Fraud Risk %"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

# -----------------------------
# SAMPLE ANALYTICS SECTION
# -----------------------------
st.subheader("📊 Transaction Insights")

sample_data = np.random.randn(200)

fig = px.histogram(sample_data, nbins=30, title="Transaction Distribution")
st.plotly_chart(fig, use_container_width=True)