# 🏥 Real-Time AI-Based Health Monitoring System
> An intelligent health anomaly detection system that monitors vital signs in real-time using Machine Learning.

### 📋 About The Project
This project simulates real-time health monitoring of a patient by tracking three critical vitals: Heart Rate, SpO2, and Body Temperature. It uses **Isolation Forest** algorithm to detect anomalies that could indicate a health emergency.

**Project - Anomaly Detection using Isolation Forest**

### ✨ Key Features
- 🤖 **AI Model Training:** Trains on 1000 synthetic patient records
- 📡 **Real-Time Monitoring:** Simulates live sensor data stream
- 🚨 **Instant Alerts:** Detects abnormal vitals (HR: 45/115/130)
- 📊 **Smart Detection:** Uses unsupervised learning (Contamination = 0.05)

### 🧠 How It Works
1. **Data Generation:** Creates 1000 records with `hr` (60-100), `spo2` (94-99), `temp` (36.0-37.5)
2. **Anomaly Injection:** 5% data injected with critical values for training
3. **Model Training:** `IsolationForest(contamination=0.05, random_state=42)`
4. **Live Monitoring:** Model predicts `-1` for anomaly, `1` for normal

### 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** pandas, random, time, scikit-learn
- **Algorithm:** Isolation Forest (Unsupervised Anomaly Detection)

### Overview
This project monitors real-time health vitals and detects anomalies using AI.

### 🚀 How to Run
```bash
# Install dependencies
pip install pandas scikit-learn

# Run the project
python final_project.py
```

### 📸 Demo Result (Live)
```
Training AI model with 1000 records...
AI Model Ready! Starting Real-Time Monitoring...

[Normal] HR: 78 | SpO2: 97 | Temp: 36.8 -> STATUS: NORMAL
[Normal] HR: 82 | SpO2: 96 | Temp: 36.9 -> STATUS: NORMAL
[ALERT!] HR: 130 | SpO2: 95 | Temp: 37.1 -> STATUS: ANOMALY DETECTED!
```

### 🔮 Future Scope
- Integration with IoT sensors (MAX30100, DHT11)
- Mobile App Alert System
- Cloud Dashboard with Firebase
- ECG Signal Analysis

### 👩‍💻 Author
mythri13-488 |
Project - 2025-2026 
