import RPi.GPIO as GPIO
import time

#def button_pressed(event):
	#print(f"[{time.strftime('%H:%M:%S')}] BUTTON PRESS DETECTED")

PORT_BUTTON =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def run_btn_loop(delay,callback,stop_event):   
    while not stop_event.is_set():
        state = GPIO.input(PORT_BUTTON) == GPIO.LOW
        callback(state)
        time.sleep(delay)