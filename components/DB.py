import threading

def run_db(settings, threads, stop_event):
    delay = 3
    if settings["simulated"]:
        from simulators.DB import run_db_simulator
        t = threading.Thread(
            target=run_db_simulator,
            args=(delay, stop_event)
        )
        t.start()
        threads.append(t)
