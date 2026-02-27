import random
import time

def run_ir_simulator(delay, callback, stop_event):

    colors = [
        (100,0,0),
        (0,100,0),
        (0,0,100),
        (100,100,0),
        (0,100,100),
        (100,0,100)
    ]

    while not stop_event.is_set():
        r,g,b = random.choice(colors)
        callback(r,g,b)
        time.sleep(delay)