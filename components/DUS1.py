#from sensors.DUS1 import run_dus1_loop
from simulators.DUS1 import run_dus1_simulator
import threading
import time

def run_dus1(settings,data_queue, threads, stop_event):
        def dus1_callback(distance):
            data_queue.put((
                "iot/pi1/dus1",
                {
                    "value": distance,
                    "simulated": settings["simulated"],
                }
            ))
        if settings['simulated']==True:
            dus1_thread = threading.Thread(target = run_dus1_simulator, args=(2, dus1_callback, stop_event))
            print("Dus1 sumilator started")
            dus1_thread.start()
            threads.append(dus1_thread)
        else:
            """
            dus1_thread = threading.Thread(target=run_dus1_loop, args=(2, dus1_callback, stop_event))
            print("Dus1 loop started")
            dus1_thread.start()
            threads.append(dus1_thread)
                
            """
            print("Real sensor implementation.")