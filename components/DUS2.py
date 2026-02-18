#from sensors.DUS2 import run_dus2_loop
from simulators.DUS2 import run_dus2_simulator
import threading
import time
from people_counter_controller import PeopleCounterController

def run_dus2(settings,data_queue, threads, stop_event,people_controller):
        def dus2_callback(distance):
            people_controller.add_distance(distance)
            data_queue.put((
                "iot/pi2/dus2",
                {
                    "value": distance,
                    "simulated": settings["simulated"],
                }
            ))
        if settings['simulated']==True:
            dus2_thread = threading.Thread(target = run_dus2_simulator, args=(2, dus2_callback, stop_event))
            print("Dus2 sumilator started")
            dus2_thread.start()
            threads.append(dus2_thread)
        else:
            """
            dus2_thread = threading.Thread(target=run_dus2_loop, args=(2, dus2_callback, stop_event))
            print("Dus2 loop started")
            dus2_thread.start()
            threads.append(dus2_thread)
                
            """
            print("Real sensor implementation.")