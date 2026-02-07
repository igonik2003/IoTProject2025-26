import threading
from simulators.DB import run_db_simulator

def run_db(settings, data_queue, threads, stop_event):

    def db_callback(state: bool):
        data_queue.put((
            "iot/pi1/db",
            {
                "value": int(state),
                "simulated": settings["simulated"]
            }
        ))

    t = threading.Thread(
        target=run_db_simulator,
        args=(3, db_callback, stop_event),
        daemon=True
    )
    t.start()
    threads.append(t)
