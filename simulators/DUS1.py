import time
import random

def generate_values(initial_distance = 25):
      distance = initial_distance
      while True:
            distance = distance + random.randint(-3, 3)
            if distance < 0:
                  distance = 0
            if distance > 50:
                  distance = 50
            yield distance
     

def run_dus1_simulator(delay, callback, stop_event):
        for d in generate_values():
            time.sleep(delay) 
            callback(d)
            if stop_event.is_set():
                  break