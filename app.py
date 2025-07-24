import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model
with open("kidney_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="CKD Prediction App")
st.title("🔬 Chronic Kidney Disease Prediction")

st.markdown("Enter patient details to predict whether they have CKD.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=35)
bp = st.number_input("Blood Pressure (mmHg)", value=80)
sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025])
al = st.slider("Albumin", 0, 5, 0)
su = st.slider("Sugar", 0, 5, 0)
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["notpresent", "present"])
ba = st.selectbox("Bacteria", ["notpresent", "present"])
bgr = st.number_input("Blood Glucose Random (mg/dL)", value=110)
bu = st.number_input("Blood Urea (mg/dL)", value=30)
sc = st.number_input("Serum Creatinine (mg/dL)", value=1.0)
sod = st.number_input("Sodium (mEq/L)", value=135)
pot = st.number_input("Potassium (mEq/L)", value=4.5)
hemo = st.number_input("Hemoglobin (g/dL)", value=14)
pcv = st.number_input("Packed Cell Volume", value=40)
wc = st.number_input("White Blood Cell Count", value=8000)
rc = st.number_input("Red Blood Cell Count (millions/cmm)", value=5.0)
htn = st.selectbox("Hypertension", ["no", "yes"])
dm = st.selectbox("Diabetes Mellitus", ["no", "yes"])
cad = st.selectbox("Coronary Artery Disease", ["no", "yes"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["no", "yes"])
ane = st.selectbox("Anemia", ["no", "yes"])

# Mapping categorical inputs to numeric
def map_input(val, positive="yes"):
    return 1 if val == positive else 0

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

# Predict button
if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    result = "✅ CKD Detected" if prediction == 1 else "🟢 No CKD Detected"
    st.subheader(f"Prediction: {result}")
