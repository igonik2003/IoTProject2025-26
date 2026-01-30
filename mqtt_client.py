import paho.mqtt.client as mqtt

def create_mqtt_client(settings):
    client = mqtt.Client()
    client.connect(
        settings["mqtt"]["host"],
        settings["mqtt"]["port"],
        60
    )
    client.loop_start()
    return client