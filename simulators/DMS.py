import time
import random

def run_dms_simulator(delay, stop_event):
    while not stop_event.is_set():
        if random.randint(0, 5) == 1:
            print(f"[{time.strftime('%H:%M:%S')}] DMS: ACTIVATED")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] DMS: inactive")
        time.sleep(delay)

def activate(pin=None):
    print("DMS: ACTIVATED (simulator)")

def deactivate(pin=None):
    print("DMS: DEACTIVATED (simulator)")
