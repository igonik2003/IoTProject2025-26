#from sensors.DPIR2 import run_dpir2_loop
from simulators.DPIR2 import run_dpir2_simulator
import threading
import time
from people_counter_controller import PeopleCounterController


def run_dpir2(settings,data_queue, threads, stop_event,people_controller):
        def dpir2_callback(motion_detected: bool):
            data_queue.put((
                "iot/pi2/dpir2",
                {
                    "value": motion_detected,
                    "simulated": settings["simulated"],
                }
            ))
            if motion_detected:
                people_controller.motion_triggered()
                
        if settings['simulated']==True:
            dpir2_thread = threading.Thread(target = run_dpir2_simulator, args=(2,dpir2_callback,stop_event))
            print("Dpir2 sumilator started")
            dpir2_thread.start()
            threads.append(dpir2_thread)
        else:
            """
            dpir2_thread = threading.Thread(target=run_dpir2_loop, args=(2,dpir2_callback,stop_event))
            print("Dpir2 loop started")    
            dpir2_thread.start()
            threads.append(dpir2_thread)
            """
            print("Real sensor implementation.")   