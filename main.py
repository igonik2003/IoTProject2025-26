import threading
from settings import load_settings
from components.DUS1 import run_dus1
from components.DPIR import run_dpir1
from components.DS1 import run_ds1
from components.DL import run_dl
from components.DB import run_db
from components.DMS import run_dms
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop

import time

if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()

    data_queue = queue.Queue(maxsize=1000)
    mqtt_client = create_mqtt_client(settings)
    mqtt_thread = threading.Thread(
        target=mqtt_publisher_loop,
        args=(mqtt_client, data_queue, stop_event),
        daemon=True
    )
    mqtt_thread.start()
    try:
        dus1_settings = settings['sensors']['DUS1']
        run_dus1(dus1_settings,data_queue, threads, stop_event)
        dpir1_settings = settings['sensors']['DPIR1']
        run_dpir1(dpir1_settings,data_queue, threads, stop_event)
        ds1_settings = settings['sensors']['DS1']
        run_ds1(ds1_settings,data_queue, threads, stop_event)
        #dl_settings = settings['sensors']["DL"]
        #run_dl(dl_settings, threads, stop_event)
        #db_settings = settings['sensors']["DB"]
        #run_db(db_settings, threads, stop_event)
        #dms_settings = settings['sensors']["DMS"]
        #run_dms(dms_settings, threads, stop_event)
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()
