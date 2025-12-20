import time
import random
    

def run_dpir1_simulator(delay,stop_event):
    while True:
        motion_detected = random.randint(0, 5) == 1
        
        if motion_detected:
            print(f"[{time.strftime('%H:%M:%S')}] You moved")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] You stopped moving.")
            
        if stop_event.is_set():
            break

        time.sleep(delay)
