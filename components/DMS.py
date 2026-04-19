import threading
from simulators.DMS import run_dms_simulator

def run_dms(settings, data_queue, threads, stop_event, pin_controller):

    def dms_callback(digit):
        data_queue.put((
            "iot/pi1/dms",
            {
                "value": digit,
                "simulated": settings["simulated"]
            }
        ))

        pin_controller.enter_digit(digit)

    t = threading.Thread(
        target=run_dms_simulator,
        args=(4, dms_callback, stop_event),
        daemon=True
    )
    t.start()
    threads.append(t)
