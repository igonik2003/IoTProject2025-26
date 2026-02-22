import RPi.GPIO as GPIO
import time

PORT_BUTTON =17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PORT_BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def run_btn_loop(delay,callback,stop_event):   
    GPIO.add_event_detect(PORT_BUTTON, GPIO.RISING, callback = callback(True), bouncetime = 100)
