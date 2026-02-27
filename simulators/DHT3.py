import time
import random

def generate_values():
    while True:
        temperature = round(random.uniform(19, 29), 2)
        humidity = round(random.uniform(40, 80), 2)
        yield temperature, humidity

def run_dht3_simulator(delay, callback, stop_event):
    for t, h in generate_values():
        time.sleep(delay)
        callback(t, h)
        if stop_event.is_set():
            break