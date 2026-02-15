import threading
from settings import load_settings
from components.DPIR3 import run_dpir3
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop

import time

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
    try:
        dpir3_settings = settings['sensors']['DPIR3']
        run_dpir3(dpir3_settings,data_queue, threads, stop_event)
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()