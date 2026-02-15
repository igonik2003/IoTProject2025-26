import time
import random
    
def run_btn_simulator(delay,callback,stop_event):
    while not stop_event.is_set():
        button_pressed = random.randint(0, 5) == 1

        callback(button_pressed)

        time.sleep(delay)