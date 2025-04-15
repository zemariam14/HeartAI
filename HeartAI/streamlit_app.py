import streamlit as st
import requests

# Sidebar
st.sidebar.title("HeartAI")
st.sidebar.caption("By Zemariam Ephrem")
st.sidebar.markdown("A machine learning tool for predicting heart disease risk.")

# Page title
st.title("Heart Disease Risk Predictor")

st.markdown("### Enter your health information below:")

# ========== Personal Info ==========
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.radio("Sex", ["Male", "Female"])
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", [0, 1])

with col2:
    trestbps = st.number_input("Resting Blood Pressure", 80, 200)
    chol = st.number_input("Cholesterol", 100, 400)
    thalch = st.number_input("Max Heart Rate", 60, 220)

# ========== Heart & ECG ==========
st.markdown("---")
st.markdown("### ECG and Angina Details")

col3, col4 = st.columns(2)

with col3:
    restecg = st.selectbox("Resting ECG", ["normal", "ST-T abnormality", "left ventricular hypertrophy"])
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Oldpeak", 0.0, 6.0, step=0.1)

with col4:
    slope = st.selectbox("Slope", ["upsloping", "flat", "downsloping"])
    ca = st.number_input("Number of Major Vessels", 0, 3)
    thal = st.selectbox("Thalassemia", ["normal", "fixed defect", "reversable defect"])

# ========== Chest Pain ==========
cp = st.selectbox("Chest Pain Type", [
    "typical angina",
    "atypical angina",
    "non-anginal pain",
    "asymptomatic"
])

# ========== Validation ==========
if age < 18:
    st.warning("Model not validated on minors under 18.")
if chol < 100:
    st.warning("Cholesterol value is unusually low.")
if trestbps < 80 or trestbps > 200:
    st.warning("Resting blood pressure is outside typical human range.")
if thalch < 60:
    st.warning("Maximum heart rate is quite low.")

# ========== Prepare JSON and convert ==========
input_data = {
    "age": age,
    "sex": 1 if sex == "Male" else 0,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalch": thalch,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal,
    "cp": cp
}

# ========== Submit & Result ==========
if st.button("Predict"):
    try:
        response = requests.post("http://localhost:8000/api/predict", json=input_data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            if prediction == 1:
                st.error("Prediction: Likely Heart Disease")
            else:
                st.success("Prediction: No Heart Disease Detected")
        else:
            st.error(f"API Error: {response.status_code}")
    except Exception as e:
        st.error(f"Connection failed: {e}")
