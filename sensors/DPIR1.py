import RPi.GPIO as GPIO
import time
import random

PIR_PIN =21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def run_dpir1_loop(delay,callback,stop_event):
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=lambda x:callback(True))