import time
import random
    
def run_btn_simulator(delay,callback,stop_event):
    while not stop_event.is_set():
        button_pressed = random.randint(0, 3) == 1

        print("Pritisnuto:",button_pressed)
        callback(button_pressed)

        time.sleep(delay)