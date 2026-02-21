#from sensors.DPIR3 import run_dpir3_loop
from simulators.DPIR3 import run_dpir3_simulator
import threading
import time
import random


def run_dpir3(settings,data_queue, threads, stop_event,security_controller):
        def dpir3_callback(motion_detected: bool):
            data_queue.put((
                "iot/pi3/dpir3",
                {
                    "value": motion_detected,
                    "simulated": settings["simulated"],
                }
            ))
            if motion_detected:
                r=random.randint(0, 5)
                print("Broj ljudi u kuci",r)
                security_controller.update_people_count(r)
                data_queue.put((
                    "iot/pi3/people_count",
                    {
                        "value": r,
                        "simulated": settings["simulated"]
                    }
                ))
                security_controller.motion_detected()

        if settings['simulated']==True:
            dpir3_thread = threading.Thread(target = run_dpir3_simulator, args=(2,dpir3_callback,stop_event))
            print("Dpir3 sumilator started")
            dpir3_thread.start()
            threads.append(dpir3_thread)
        else:
            """
            dpir3_thread = threading.Thread(target=run_dpir3_loop, args=(2,dpir3_callback,stop_event))
            print("Dpir3 loop started")    
            dpir3_thread.start()
            threads.append(dpir3_thread)
            """
            print("Real sensor implementation.")   