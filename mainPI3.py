import threading
from settings import load_settings
from components.DPIR3 import run_dpir3
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop
from components.DB import run_db
from security_alarm_controller import SecurityAlarmController
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
    db_activate, db_deactivate = run_db(settings['sensors']['DB'], data_queue, threads, stop_event)

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
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()