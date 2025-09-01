# backend/anomaly_detection.py
from sklearn.ensemble import IsolationForest
import numpy as np

# Dummy model trained on normal ranges
model = IsolationForest(contamination=0.1, random_state=42)
model.fit([[25, 50, 0], [26, 55, 1], [24, 48, 0], [27, 52, 0]])

def check_for_anomaly(point):
    point = np.array(point).reshape(1, -1)
    result = model.predict(point)[0]
    return result == -1
