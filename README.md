# 🚗 Predictive Maintenance for Fleet Vehicles

## 📌 Overview
This project demonstrates an end-to-end machine learning pipeline to predict potential vehicle failures using sensor data.

It covers:
- Data preprocessing  
- Model development  
- Evaluation  
- Deployment using Streamlit  

---

## 🎯 Problem Statement
Fleet vehicles often experience unexpected failures due to lack of predictive insights, leading to:

- Increased downtime  
- Higher maintenance costs  
- Operational inefficiencies  

👉 This project predicts failure risks early using sensor data.

---

## 🧠 Solution Approach

### 🔹 Features Used
- Engine Temperature  
- Vibration Levels  
- RPM  
- Error Count  
- Battery Voltage  

---

## 📸 Dataset Preview

![Dataset](images/dataset.png)

---

## 🤖 Model Development

- Algorithm: Random Forest Classifier  
- Train-Test Split: 80-20  
- Objective: Binary classification  

---

## 📸 Model Output

![Model Output](images/model_output.png)

---

## 📊 Model Performance

- Accuracy: ~70%  
- Balanced precision and recall  

⚠️ Note:  
This is a proof-of-concept with simulated labels.

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- scikit-learn  
- Matplotlib  
- Streamlit  

---

## 🌐 Run the App

```bash
pip install -r requirements.txt
streamlit run app.py

💼 Business Impact
- Enables proactive maintenance
- Reduces unexpected failures
- Improves efficiency

🚀 Future Improvements
- Use real failure labels
- Add time-series models
- Deploy as API
