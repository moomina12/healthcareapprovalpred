#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

st.title("🏥 Healthcare Claim Prediction System")

st.sidebar.header("Enter Claim Details")

# User Inputs
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.sidebar.radio("Gender", ["Male", "Female"])
condition = st.sidebar.selectbox("Condition", ["Back Pain", "Knee Injury", "Fracture", "Other"])
session_count = st.sidebar.number_input("Session Count", min_value=1, max_value=20, value=5)
claimed_amount = st.sidebar.number_input("Claimed Amount ($)", min_value=100, max_value=5000, value=800)
reschedule_count = st.sidebar.number_input("Reschedule Count", min_value=0, max_value=10, value=1)

if st.sidebar.button("Predict"):
    # Send request to FastAPI
    url = "http://127.0.0.1:8000/predict/"
    data = {
        "age": age,
        "gender": gender,
        "condition": condition,
        "session_count": session_count,
        "claimed_amount": claimed_amount,
        "reschedule_count": reschedule_count
    }

    response = requests.post(url, json=data)
    result = response.json()

    # Display results
    st.subheader("📌 Prediction Results")
    st.success(f"**Predicted Claim Status:** {result['Approval_Status']}")
    st.info(f"**Predicted Settled Amount:** ${result['Predicted_Revenue']:.2f}")

