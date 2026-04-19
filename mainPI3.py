import threading
from settings import load_settings
from components.DPIR3 import run_dpir3
from components.DHT1 import run_dht1
from components.DHT2 import run_dht2
from components.LCD import LCDManager
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop
from components.DB import run_db
from components.BRGB import run_brgb
from components.IR import run_ir
from security_alarm_controller import SecurityAlarmController
import time
import json

if __name__ == "__main__":
    print('Starting PI3')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()

    data_queue = queue.Queue(maxsize=1000)
    mqtt_client = create_mqtt_client(settings)
    mqtt_thread = threading.Thread(
        target=mqtt_publisher_loop,
        args=(mqtt_client, data_queue, stop_event, settings),
        daemon=True
    )
    mqtt_thread.start()
    db_activate, db_deactivate = run_db(settings['sensors']['DB'], data_queue, threads, stop_event)
    lcd_manager = LCDManager(settings["sensors"]["LCD"])

    security_controller = SecurityAlarmController(
        settings['sensors']['DB']['simulated'],
        data_queue,
        db_activate,
        db_deactivate
    )
    data_queue.put((
        "iot/house/alarm",
        {
            "value": 0,
            "simulated": settings['sensors']['DB']['simulated']
        }
    ))
    def publish_people_count(count):
        data_queue.put((
            "iot/pi3/people_count",
            {
                "value": count,
                "simulated": settings['sensors']['DPIR3']["simulated"]
            }
    ))
    publish_people_count(0)
    try:
        dpir3_settings = settings['sensors']['DPIR3']
        run_dpir3(dpir3_settings,data_queue, threads, stop_event,security_controller)
        dht1_settings = settings["sensors"]["DHT1"]
        run_dht1(dht1_settings, data_queue, threads, stop_event, lcd_manager)
        dht2_settings = settings["sensors"]["DHT2"]
        run_dht2(dht2_settings, data_queue, threads, stop_event, lcd_manager)
        brgb_settings = settings["sensors"]["BRGB"]
        brgb_controller = run_brgb(brgb_settings, data_queue, threads, stop_event)
        ir_settings = settings["sensors"]["IR"]
        run_ir(ir_settings, data_queue, threads, stop_event, brgb_controller)
        def on_message(client, userdata, msg):

            if msg.topic == "iot/pi3/brgb":

                payload = json.loads(msg.payload.decode())

                r = payload.get("r", 0)
                g = payload.get("g", 0)
                b = payload.get("b", 0)

                print(f"WEB RGB COMMAND -> R:{r} G:{g} B:{b}")

                brgb_controller(r, g, b)

        mqtt_client.subscribe("iot/pi3/brgb")
        mqtt_client.on_message = on_message
        mqtt_client.loop_start()
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()