
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("🚗 Predictive Maintenance App")

st.write("Enter vehicle sensor data to predict failure risk.")

# Inputs
engine_temp = st.slider("Engine Temperature (°C)", 60, 140, 95)
vibration = st.slider("Vibration (mm/s)", 0.5, 15.0, 5.0)
rpm = st.slider("RPM", 800, 5000, 2500)
error_codes = st.slider("Error Code Count", 0, 10, 2)
battery = st.slider("Battery Voltage", 10.0, 15.0, 12.5)

# Dummy training data
X = pd.DataFrame({
    "engine_temp": np.random.normal(95, 10, 200),
    "vibration": np.random.normal(5, 2, 200),
    "rpm": np.random.normal(2500, 400, 200),
    "error_codes": np.random.randint(0, 10, 200),
    "battery": np.random.normal(12.5, 1, 200)
})

y = ((X["engine_temp"] > 100) | (X["vibration"] > 6) | (X["error_codes"] > 5)).astype(int)

model = RandomForestClassifier()
model.fit(X, y)

# Prediction
input_data = pd.DataFrame({
    "engine_temp": [engine_temp],
    "vibration": [vibration],
    "rpm": [rpm],
    "error_codes": [error_codes],
    "battery": [battery]
})

prediction = model.predict(input_data)[0]
prob = model.predict_proba(input_data)[0][1]

st.subheader("Prediction Result")

if prediction == 1:
    st.error(f"⚠️ High Failure Risk ({prob:.2f})")
else:
    st.success(f"✅ Low Failure Risk ({prob:.2f})")

