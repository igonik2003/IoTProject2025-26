import time
import random

def run_gsg_simulator(delay, callback, stop_event):

    while not stop_event.is_set():

        movement = random.random() < 0.1  # 10% šanse

        callback(movement)

        time.sleep(delay)