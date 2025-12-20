import RPi.GPIO as GPIO
import time

PIR_PIN =4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def motion_detected(channel):
    print(f"[{time.strftime('%H:%M:%S')}] You moved")

def no_motion(channel):
    print(f"[{time.strftime('%H:%M:%S')}] You stopped moving")

def run_dpir1_loop(delay,stop_event):   
    while True:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion_detected)
        GPIO.add_event_detect(PIR_PIN, GPIO.FALLING, callback=no_motion)

        if stop_event.is_set():
            break

        time.sleep(delay)   