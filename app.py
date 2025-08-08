import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("kidney_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="CKD Prediction App", layout="wide")
st.title("🔬 Chronic Kidney Disease (CKD) Predictor")
st.markdown("Use the form below to enter patient details and predict the likelihood of CKD.")

st.divider()

# Categorical mapping function
def map_input(val, positive="yes"):
    return 1 if val == positive else 0

# ---- Input Section ----
st.subheader("📋 Patient Vitals & Lab Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=35)
    bp = st.number_input("Blood Pressure (mmHg)", value=80)
    sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
    al = st.slider("Albumin", 0, 5, 0)
    su = st.slider("Sugar", 0, 5, 0)

with col2:
    bgr = st.number_input("Blood Glucose Random (mg/dL)", value=110)
    bu = st.number_input("Blood Urea (mg/dL)", value=30)
    sc = st.number_input("Serum Creatinine (mg/dL)", value=1.0)
    sod = st.number_input("Sodium (mEq/L)", value=135)
    pot = st.number_input("Potassium (mEq/L)", value=4.5)

with col3:
    hemo = st.number_input("Hemoglobin (g/dL)", value=14)
    pcv = st.number_input("Packed Cell Volume", value=40)
    wc = st.number_input("White Blood Cell Count", value=8000)
    rc = st.number_input("Red Blood Cell Count (millions/cmm)", value=5.0)

st.subheader("🧬 Cell and Urine Test Results")

col4, col5, col6 = st.columns(3)
with col4:
    rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
    pc = st.selectbox("Pus Cell", ["normal", "abnormal"])

with col5:
    pcc = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
    ba = st.selectbox("Bacteria", ["notpresent", "present"])

st.subheader("🩺 Health Conditions")

col7, col8, col9 = st.columns(3)
with col7:
    htn = st.selectbox("Hypertension", ["no", "yes"])
    dm = st.selectbox("Diabetes Mellitus", ["no", "yes"])

with col8:
    cad = st.selectbox("Coronary Artery Disease", ["no", "yes"])
    appet = st.selectbox("Appetite", ["good", "poor"])

with col9:
    pe = st.selectbox("Pedal Edema", ["no", "yes"])
    ane = st.selectbox("Anemia", ["no", "yes"])

# ---- Model Prediction ----
input_data = [
    age, bp, sg, al, su,
    map_input(rbc, "abnormal"),
    map_input(pc, "abnormal"),
    map_input(pcc, "present"),
    map_input(ba, "present"),
    bgr, bu, sc, sod, pot, hemo, pcv, wc, rc,
    map_input(htn), map_input(dm), map_input(cad),
    map_input(appet, "poor"),
    map_input(pe), map_input(ane)
]

st.divider()

# Predict button with spinner and styled output
if st.button("🔍 Predict CKD"):
    with st.spinner("Analyzing data..."):
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        
        if prediction == 1:
            st.error("🔴 Prediction: CKD Detected")
            st.markdown("The model indicates a high likelihood of Chronic Kidney Disease.")
        else:
            st.success("🟢 Prediction: No CKD Detected")
            st.markdown("The model indicates no signs of CKD based on current data.")

