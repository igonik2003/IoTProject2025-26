import json
import sys
import os
# dodaj parent directory u PYTHON PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#from paho.mqtt import client as mqtt
from mqtt_subscriber_client import create_subscriber_client
import paho.mqtt.client as mqtt
from settings import load_settings
from influxdb_client import InfluxDBClient, Point, WritePrecision

BROKER_HOST = "127.0.0.1"
BROKER_PORT = 1883
TOPIC = "iot/#"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(TOPIC)
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Failed to connect. Error code: {rc}")


def on_message(client, userdata, msg):
    influx_write_api = userdata["influx_write_api"]
    bucket = userdata["bucket"]

    try:
        payload_str = msg.payload.decode("utf-8")
        print("\n--------------------------------------------------")
        print(f"TOPIC:   {msg.topic}")
        print(f"PAYLOAD: {payload_str}")

        try:
            payload = json.loads(payload_str)
            print("Parsed JSON:", payload)
        except json.JSONDecodeError:
            print("Payload is not JSON, wrapping into raw field")
            payload = {"raw": payload_str}

        point = (
            Point("iot_measurement")        
            .tag("topic", msg.topic)       
            .field("data", json.dumps(payload))  
        )

        influx_write_api.write(bucket=bucket, record=point)
        print("Saved to InfluxDB")

    except Exception as e:
        print(f"Error handling message: {e}")



def main():
    settings = load_settings()

    influx_cfg = settings["influxdb"]
    influx_client = InfluxDBClient(
        url=influx_cfg["url"],
        token=influx_cfg["token"],
        org=influx_cfg["org"]
    )
    write_api = influx_client.write_api()
    print("InfluxDB client initialized")

    mqtt_client = create_subscriber_client(settings)

    mqtt_client.user_data_set({
        "influx_write_api": write_api,
        "bucket": influx_cfg["bucket"]
    })

    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    print("Starting MQTT client...")
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()