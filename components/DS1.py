#from actuators.DS1 import run_ds1_loop
from simulators.DS1 import run_ds1_simulator
import threading
import time     

def run_ds1(settings,data_queue, threads, stop_event):
    def ds1_callback(button_pressed: bool):
        data_queue.put((
            "iot/pi1/ds1",
            {
                "value": button_pressed,
                "simulated": settings["simulated"],
            }
        ))
    if settings['simulated']==True:
        ds1_thread = threading.Thread(target = run_ds1_simulator, args=(2,ds1_callback,stop_event))
        print("Ds1 sumilator started")
        ds1_thread.start()
        threads.append(ds1_thread)
    else:
        """
        ds1_thread = threading.Thread(target=run_ds1_loop, args=(2,ds1_callback,stop_event))
        print("Ds1 loop started")    
        ds1_thread.start()
        threads.append(ds1_thread)
        """
        print("Real sensor implementation.")                     
