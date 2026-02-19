import threading
from settings import load_settings
from components.DUS2 import run_dus2
from components.DPIR2 import run_dpir2
from components.DS2 import run_ds2
from components.BTN import run_btn
from components.SD4 import run_4sd
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop
from people_counter_controller import PeopleCounterController
from alarm_controller import AlarmController
from components.DB import run_db

import time

if __name__ == "__main__":
    print('Starting PI2')
    time4SD="13:42"
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

    alarm_controller = AlarmController(
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
            "iot/pi2/people_count",
            {
                "value": count,
                "simulated": settings['sensors']['DUS2']["simulated"]
            }
    ))
    publish_people_count(0)
    people_controller = PeopleCounterController(publish_people_count)  
    try:
        dus2_settings = settings['sensors']['DUS2']
        run_dus2(dus2_settings,data_queue, threads, stop_event,people_controller)
        dpir2_settings = settings['sensors']['DPIR2']
        run_dpir2(dpir2_settings,data_queue, threads, stop_event,people_controller)
        ds2_settings = settings['sensors']['DS2']
        run_ds2(ds2_settings,data_queue, threads, stop_event,alarm_controller)
        btn_settings = settings['sensors']["BTN"]
        run_btn(btn_settings, data_queue, threads, stop_event)
        sd_settings = settings['sensors']['SD4']
        run_4sd(sd_settings,time4SD,data_queue, threads, stop_event)

        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()