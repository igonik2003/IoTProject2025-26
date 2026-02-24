from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os
from influxdb_client import InfluxDBClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from settings import load_settings
from pydantic import BaseModel
import json
from mqtt_client import create_mqtt_client

app = FastAPI()

# Dozvoli Angular aplikaciji da pristupi backendu
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = load_settings()
mqtt_client = create_mqtt_client(settings)

influx_cfg = settings["influxdb"]

influx_client = InfluxDBClient(
    url=influx_cfg["url"],
    token=influx_cfg["token"],
    org=influx_cfg["org"]
)

query_api = influx_client.query_api()
bucket = influx_cfg["bucket"]

class TimerSettings(BaseModel):
    seconds: int

class TimerSettings1(BaseModel):
    addSeconds: int

@app.post("/api/timer/settings")
def set_timer(time_setting:TimerSettings):
    payload = {
        "seconds": time_setting.seconds,
    }
    #print(payload["seconds"],payload["addSeconds"])
    mqtt_client.publish(
        "iot/pi2/timer/settings",
        json.dumps(payload)
    )

    return {"status": "sent to pi2"}

@app.post("/api/timer/settings1")
def set_timer1(time_setting:TimerSettings1):
    payload = {
        "addSeconds": time_setting.addSeconds
    }
    #print(payload["seconds"],payload["addSeconds"])
    mqtt_client.publish(
        "iot/pi2/timer/settings1",
        json.dumps(payload)
    )

    return {"status": "sent to pi2"}
@app.get("/sensor/{pi_id}/{sensor_id}")
def get_sensor_data(pi_id: str, sensor_id: str):

    topic = f"iot/{pi_id}/{sensor_id}"

    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -30d)
      |> filter(fn: (r) => r["_measurement"] == "iot_measurement")
      |> filter(fn: (r) => r["topic"] == "{topic}")
      |> sort(columns: ["_time"], desc: true)
      |> limit(n: 1)
      |> keep(columns: ["_time", "_value", "_field"])
      |> duplicate(column: "_time", as: "timestamp")
    '''

    result = query_api.query(query)

    if not result:
        return {"error": "No data found"}

    data_value = None
    simulated_value = None
    time = None

    for table in result:
        for record in table.records:
            if time is None:
                time = record.values.get("timestamp")
            if record.get_field() == "data":
                data_value = record.get_value()
            if record.get_field() == "simulated":
                simulated_value = record.get_value()


    return {
        "pi": pi_id,
        "sensor": sensor_id,
        "data": data_value,
        "simulated": simulated_value,
        "time": time.strftime("%Y-%m-%dT%H:%M:%SZ") if time else None
    }
@app.get("/")
def root():
    return {"status": "Backend connected successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)