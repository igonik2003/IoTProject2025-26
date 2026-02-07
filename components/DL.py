import threading
from simulators.DL import run_dl_simulator

def run_dl(settings, data_queue, threads, stop_event):

    def dl_callback(state: int):
        data_queue.put((
            "iot/pi1/dl",
            {
                "value": state,
                "simulated": settings["simulated"]
            }
        ))

    t = threading.Thread(
        target=run_dl_simulator,
        args=(2, dl_callback, stop_event),
        daemon=True
    )
    t.start()
    threads.append(t)
