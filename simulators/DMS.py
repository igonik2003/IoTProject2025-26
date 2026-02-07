import time
import random

def run_dms_simulator(delay, callback, stop_event):
    while not stop_event.is_set():
        pressed = random.randint(0, 5) == 1
        callback(pressed)
        time.sleep(delay)
