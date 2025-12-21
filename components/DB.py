import threading

def run_db(settings, threads, stop_event):
    simulated = settings["simulated"]
    pin = settings["pin"]

    if simulated:
        from simulators.DB import beep
    else:
        from actuators.DB import setup, beep
        setup(pin)

    def loop():
        while not stop_event.is_set():
            cmd = input("DB (beep): ").strip().lower()
            if cmd == "beep":
                beep(pin)

    t = threading.Thread(target=loop)
    t.start()
    threads.append(t)
