import time
import random

def run_db_simulator(delay, callback, stop_event):
    while not stop_event.is_set():
        active = random.randint(0, 4) == 2 
        callback(active)
        time.sleep(delay)
