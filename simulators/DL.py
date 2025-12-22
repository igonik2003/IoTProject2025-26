import time
import random

def run_dl_simulator(delay, stop_event):
    while not stop_event.is_set():
        value = random.randint(0, 3)
        if value == 1:
            print(f"[{time.strftime('%H:%M:%S')}] DL: LED ON")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] DL: LED OFF")
        time.sleep(delay)
