import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("🚗 Predictive Maintenance App")
st.write("Enter vehicle sensor data to predict failure risk.")

# --- Load the REAL dataset (same one used in the notebook) ---
df = pd.read_csv("sample_vehicle_sensor_data.csv")

# --- Recreate the exact same labels as the notebook ---
np.random.seed(42)

df['failure_risk'] = (
    (df['engine_temp_c'] > 95) |
    (df['vibration_mm_s'] > 5) |
    (df['error_code_count'] >= 2) |
    (df['battery_voltage'] < 12.0)
).astype(int)

# Introduce the same realistic label noise as the notebook
flip_mask = np.random.rand(len(df)) < 0.10
df.loc[flip_mask, 'failure_risk'] = 1 - df.loc[flip_mask, 'failure_risk']

X = df[['engine_temp_c', 'vibration_mm_s', 'avg_rpm', 'error_code_count', 'battery_voltage']]
y = df['failure_risk']

# --- Train once, with the same split settings as the notebook ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# --- User inputs ---
engine_temp = st.slider("Engine Temperature (°C)", 60, 140, 95)
vibration = st.slider("Vibration (mm/s)", 0.5, 15.0, 5.0)
rpm = st.slider("RPM", 800, 5000, 2500)
error_codes = st.slider("Error Code Count", 0, 10, 2)
battery = st.slider("Battery Voltage", 10.0, 15.0, 12.5)

input_data = pd.DataFrame({
    "engine_temp_c": [engine_temp],
    "vibration_mm_s": [vibration],
    "avg_rpm": [rpm],
    "error_code_count": [error_codes],
    "battery_voltage": [battery]
})

prediction = model.predict(input_data)[0]
prob = model.predict_proba(input_data)[0][1]

st.subheader("Prediction Result")
if prediction == 1:
    st.error(f"⚠️ High Failure Risk ({prob:.2f})")
else:
    st.success(f"✅ Low Failure Risk ({prob:.2f})")

st.caption("Model trained on real sensor data with domain-based failure thresholds (see GitHub README for methodology).")
