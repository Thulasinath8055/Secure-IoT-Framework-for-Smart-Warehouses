# api/main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from backend.database import insert_sensor_data
from backend.encryption import decrypt_data
from backend.anomaly_detection import check_for_anomaly

app = FastAPI()

class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float
    movement: int

@app.post("/ingest")
def ingest(data: SensorData):
    # Simulate decryption
    decrypted_data = data.dict()  # Replace with decrypt_data if encrypted
    print(f"[API] Received data: {decrypted_data}")

    # Store in DB
    insert_sensor_data(decrypted_data)

    # Anomaly detection
    is_anomaly = check_for_anomaly(
        [decrypted_data["temperature"], decrypted_data["humidity"], decrypted_data["movement"]]
    )

    if is_anomaly:
        print("[ALERT] Anomaly detected!")

    return {"status": "ok", "anomaly": is_anomaly}
