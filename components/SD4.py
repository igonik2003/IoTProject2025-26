#from actuators.SD4 import run_4sd_loop
from simulators.SD4 import run_4sd_simulator
import threading

def run_4sd(settings,time,data_queue, threads, stop_event):

    def sd_callback(time: str):
        data_queue.put((
            "iot/pi2/4sd",
            {
                "value": time,
                "simulated": settings["simulated"],
            }
        ))

    if settings["simulated"] == True:

        sd_thread = threading.Thread(
            target=run_4sd_simulator,
            args=(1, sd_callback, stop_event)
        )

        print("4sd simulator started")
        sd_thread.start()
        threads.append(sd_thread)

    else:

       """ sd_thread = threading.Thread(
            target=run_4sd_loop,
            args=(0.01,time, sd_callback, stop_event)
        )

        print("4sd real actuator started")
        sd_thread.start()
        threads.append(sd_thread)"""