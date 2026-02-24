#from sensors.DS2 import run_ds2_loop
from simulators.DS2 import run_ds2_simulator
import threading
import time     
from alarm_controller import AlarmController

def run_ds2(settings,data_queue, threads, stop_event,alarm_controller):
    
    def ds2_callback(button_pressed: bool):
        alarm_controller.process_ds2(button_pressed)
        data_queue.put((
            "iot/pi2/ds2",
            {
                "value": button_pressed,
                "simulated": settings["simulated"],
            }
        ))
    if settings['simulated']==True:
        ds2_thread = threading.Thread(target = run_ds2_simulator, args=(2,ds2_callback,stop_event))
        print("Ds2 sumilator started")
        ds2_thread.start()
        threads.append(ds2_thread)
    else:
        """
        ds2_thread = threading.Thread(target=run_ds2_loop, args=(2,ds2_callback,stop_event))
        print("Ds2 loop started")    
        ds2_thread.start()
        threads.append(ds2_thread)
        """
        print("Real sensor implementation.")    