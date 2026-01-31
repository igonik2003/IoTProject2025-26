import paho.mqtt.client as mqtt

def create_subscriber_client(settings):
    client = mqtt.Client()
    client.connect(
        settings["mqtt"]["host"],
        settings["mqtt"]["port"],
        60
    )
    return client