import threading
from simulators.GSG import run_gsg_simulator
from sensors.GSG import run_gsg_loop

def run_gsg(settings, data_queue, threads, stop_event, security_controller, get_system_armed):

    def gsg_callback(movement):

        print(f"GSG movement detected: {movement}")

        data_queue.put((
            "iot/pi2/gsg",
            {
                "value": int(movement),
                "simulated": settings["simulated"]
            }
        ))

        if movement:
            security_controller._activate_alarm()   

    if settings["simulated"]:

        t = threading.Thread(
            target=run_gsg_simulator,
            args=(2, gsg_callback, stop_event),
            daemon=True
        )
        print("GSG simulator started")

    else:

        pin = settings["pin"]

        t = threading.Thread(
            target=run_gsg_loop,
            args=(2, gsg_callback, stop_event, pin),
            daemon=True
        )
        print("GSG real sensor started")

    t.start()
    threads.append(t)