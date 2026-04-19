import RPi.GPIO as GPIO
import time

PORT_BUTTON =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def run_btn_loop(delay,callback,stop_event):   
    while not stop_event.is_set():
        current_state = GPIO.input(PORT_BUTTON)

        callback(current_state)

        time.sleep(0.1)  # polling na 100ms
