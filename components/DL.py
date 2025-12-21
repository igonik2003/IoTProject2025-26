import threading
import time

def run_dl(settings, threads, stop_event):
    simulated = settings["simulated"]
    pin = settings["pin"]

    if simulated:
        from simulators.DL import on, off
    else:
        from actuators.DL import setup, on, off
        setup(pin)

    def loop():
        while not stop_event.is_set():
            cmd = input("DL (on/off): ").strip().lower()
            if cmd == "on":
                on(pin)
            elif cmd == "off":
                off(pin)

    t = threading.Thread(target=loop)
    t.start()
    threads.append(t)
