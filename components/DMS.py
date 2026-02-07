import threading
from simulators.DMS import run_dms_simulator

def run_dms(settings, data_queue, threads, stop_event):

    def dms_callback(pressed: bool):
        data_queue.put((
            "iot/pi1/dms",
            {
                "value": int(pressed),
                "simulated": settings["simulated"]
            }
        ))

    t = threading.Thread(
        target=run_dms_simulator,
        args=(4, dms_callback, stop_event),
        daemon=True
    )
    t.start()
    threads.append(t)
