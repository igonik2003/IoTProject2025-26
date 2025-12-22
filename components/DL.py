import threading

def run_dl(settings, threads, stop_event):
    delay = 2
    if settings["simulated"]:
        from simulators.DL import run_dl_simulator
        t = threading.Thread(
            target=run_dl_simulator,
            args=(delay, stop_event)
        )
        t.start()
        threads.append(t)
