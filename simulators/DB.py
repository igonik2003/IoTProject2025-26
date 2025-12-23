import time
import random

def run_db_simulator(delay, stop_event):
    while not stop_event.is_set():
        if random.randint(0, 4) == 2:
            print(f"[{time.strftime('%H:%M:%S')}] DB: BUZZER BEEP")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] DB: silent")
        time.sleep(delay)
