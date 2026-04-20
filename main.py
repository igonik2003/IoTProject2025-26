import threading
from settings import load_settings
from components.DUS1 import run_dus1
from components.DPIR import run_dpir1
from components.DS1 import run_ds1
#from components.DL import run_dl
from components.DB import run_db
from components.DMS import run_dms
import queue
from mqtt_client import create_mqtt_client
from mqtt_publisher import mqtt_publisher_loop
from people_counter_controller import PeopleCounterController
import time
from alarm_controller import AlarmController
from security_alarm_controller import SecurityAlarmController
from pin_controller import PinController

if __name__ == "__main__":
    print('Starting PI1')
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
    security_controller = SecurityAlarmController(
        settings['sensors']['DB']['simulated'],
        data_queue,
        db_activate,
        db_deactivate
    )

    def pin_input_loop(pin_controller):
        while True:
            try:
                pin = input("Enter PIN: ")

                for digit in pin:
                    pin_controller.enter_digit(digit)

            except EOFError:
                print("Input closed, retrying...")
                time.sleep(1)

    pin_controller = PinController(security_controller, data_queue)
    t_pin = threading.Thread(
        target=pin_input_loop,
        args=(pin_controller,),
        daemon=True
    )
    t_pin.start()

    

    data_queue.put((
        "iot/house/alarm",
        {
            "value": 0,
            "simulated": settings['sensors']['DB']['simulated']
        }
    ))
    def publish_people_count(count):
        data_queue.put((
            "iot/pi1/people_count",
            {
                "value": count,
                "simulated": settings['sensors']['DUS1']["simulated"]
            }
        ))
    publish_people_count(0)
    people_controller = PeopleCounterController(publish_people_count,security_controller)    
    try:
        dus1_settings = settings['sensors']['DUS1']
        run_dus1(dus1_settings,data_queue, threads, stop_event, people_controller)
        dpir1_settings = settings['sensors']['DPIR1']
        run_dpir1(dpir1_settings,data_queue, threads, stop_event, people_controller,security_controller)
        ds1_settings = settings['sensors']['DS1']
        run_ds1(ds1_settings,data_queue, threads, stop_event,alarm_controller, pin_controller)
        #dl_settings = settings['sensors']["DL"]
        #run_dl(dl_settings, data_queue, threads, stop_event)
        #db_settings = settings['sensors']["DB"]
        #run_db(db_settings, data_queue, threads, stop_event)
        dms_settings = settings['sensors']["DMS"]
        run_dms(dms_settings, data_queue, threads, stop_event, pin_controller)
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()