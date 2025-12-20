import time
import random
    
def run_ds1_simulator(delay,stop_event):
    while True:
        button_click_detected = random.randint(0, 5) == 1
        
        if button_click_detected:
            print(f"[{time.strftime('%H:%M:%S')}] Button clicked")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Button not clicked.")
            
        if stop_event.is_set():
            break

        time.sleep(delay)
              