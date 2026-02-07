import time
import random

def run_dl_simulator(delay, callback, stop_event):
    while not stop_event.is_set():
        state = random.choice([0, 1])
        callback(state)
        time.sleep(delay)
