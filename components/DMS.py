import threading

def run_dms(settings, threads, stop_event):
    simulated = settings["simulated"]
    pin = settings["pin"]

    if simulated:
        from simulators.DMS import activate, deactivate
    else:
        from actuators.DMS import setup, activate, deactivate
        setup(pin)

    def loop():
        while not stop_event.is_set():
            cmd = input("DMS (on/off): ").strip().lower()
            if cmd == "on":
                activate(pin)
            elif cmd == "off":
                deactivate(pin)

    t = threading.Thread(target=loop)
    t.start()
    threads.append(t)
