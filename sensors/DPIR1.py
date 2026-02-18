import RPi.GPIO as GPIO
import time

PIR_PIN =4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def run_dpir1_loop(delay,callback,stop_event):   
     while not stop_event.is_set():
        motion = GPIO.input(PIR_PIN)
        callback(bool(motion))
        time.sleep(delay)  