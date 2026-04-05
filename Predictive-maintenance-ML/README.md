🚗 Predictive Maintenance for Fleet Vehicles
📌 Overview

This project demonstrates an end-to-end machine learning pipeline to predict potential vehicle failures using sensor data. It combines data analysis, model development, and deployment to simulate a real-world predictive maintenance solution.

The goal is to enable proactive maintenance, reduce downtime, and improve operational efficiency in fleet systems.

🎯 Problem Statement

Fleet vehicles often experience unexpected failures due to lack of predictive insights, leading to:

Increased maintenance costs
Unplanned downtime
Reduced operational efficiency

👉 This project builds a model to predict failure risk early using sensor data.

🧠 Solution Approach
🔹 Data Preparation
Loaded and explored structured vehicle sensor dataset
Selected relevant features for modeling
🔹 Features Used
Engine Temperature (engine_temp_c)
Vibration (vibration_mm_s)
Average RPM (avg_rpm)
Error Count (error_code_count)
Battery Voltage (battery_voltage)
📸 Dataset Preview
![Dataset](images/dataset.png)

Explanation:
This dataset contains key operational metrics collected from vehicles. These features help identify abnormal patterns that may indicate potential failures.

🤖 Model Development
Algorithm: Random Forest Classifier
Train-Test Split: 80-20
Target: Binary classification (failure risk)
📸 Model Code & Output
![Model Output](images/model_output.png)

Explanation:
The model is trained on selected features and evaluated using classification metrics such as precision, recall, and F1-score.

📊 Model Performance Summary
Accuracy: ~70%
Balanced precision and recall
Demonstrates ability to classify failure risk

⚠️ Note:
This is a proof-of-concept project. The target variable is simulated to demonstrate the machine learning workflow.

⚙️ Tech Stack
Programming: Python
Libraries: Pandas, NumPy, scikit-learn, Matplotlib
Environment: Jupyter Notebook / VS Code
Deployment: Streamlit
🌐 Streamlit Application

This project includes a simple interactive app for predictions.

▶️ Run Locally:
pip install -r requirements.txt
streamlit run app.py
📸 Streamlit App 

![Streamlit App](images/streamlit_app.png)


📁 Project Structure
predictive-maintenance-ml/
│
├── notebook/
│   └── Predictive_Maintenance_Notebook.ipynb
│
├── data/
│   └── sample_vehicle_sensor_data.csv
│
├── images/
│   ├── dataset.png
│   ├── model_output.png
│   └── streamlit_app.png
│
├── app.py
├── requirements.txt
└── README.md

💼 Business Impact
Enables proactive maintenance decisions
Reduces unexpected breakdowns
Improves operational efficiency
Demonstrates real-world ML application in automotive systems

🚀 Future Improvements
Use real labeled failure data
Incorporate time-series analysis
Improve model accuracy with advanced algorithms
Deploy as a cloud-based API

👨‍💻 Author

Bhagwant Singh Negi
M.S. Applied Data Analytics
