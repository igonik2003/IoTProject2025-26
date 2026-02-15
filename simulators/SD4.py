import time
from datetime import datetime

def run_4sd_simulator(delay, callback, stop_event):
    while not stop_event.is_set():

        simulated_time = datetime.now().strftime("%H:%M")

       #print(f"[SIMULATOR] Display shows: {simulated_time}")

        callback(simulated_time)

        time.sleep(delay)