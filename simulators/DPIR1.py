import time
import random
import datetime    

def run_dpir1_simulator(delay,callback,stop_event):
    while not stop_event.is_set():
        motion_detected = random.randint(0, 3) == 1

        print("Pokret:",motion_detected,datetime.datetime.now())
        callback(motion_detected)

        time.sleep(delay)