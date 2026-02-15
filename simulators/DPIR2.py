import time
import random
    

def run_dpir2_simulator(delay,callback,stop_event):
    while not stop_event.is_set():
        motion_detected = random.randint(0, 5) == 1

        callback(motion_detected)

        time.sleep(delay)