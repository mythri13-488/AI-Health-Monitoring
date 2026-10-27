import pandas as pd
import random
import time
from sklearn.ensemble import IsolationForest

print("Training AI model with 1000 records...")
data = []
for i in range(1000):
    hr = random.randint(60, 100)
    spo2 = random.randint(94, 99)
    temp = round(random.uniform(36.0, 37.5), 1)
    if random.random() < 0.05:
        hr = random.choice([45, 115, 130])
    data.append([hr, spo2, temp])

df = pd.DataFrame(data, columns=['heart_rate','spo2','temp'])
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)
print("AI Model Ready! Starting Real-Time Monitoring...\n")
print("Press ctrl+C to stop\n")

try:
    while True:
        hr = random.randint(60, 110)
        spo2 = random.randint(92, 99)
        temp = round(random.uniform(36.0, 38.0), 1)
        if random.random() < 0.15:
            hr = random.choice([45, 125])
        test_data = pd.DataFrame([[hr, spo2, temp]], columns=['heart_rate','spo2','temp'])
        prediction = model.predict(test_data)
        status = "NORMAL"
        if prediction[0] == -1:
            status = "AI ALERT: ANOMALY DETECTED - HIGH RISK!"
        print(f"HR: {hr} | SpO2: {spo2} | Temp: {temp}C -> {status}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n\nMonitoring stopped by user - Thank you!")