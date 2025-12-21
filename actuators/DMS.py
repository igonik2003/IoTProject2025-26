import RPi.GPIO as GPIO

def setup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

def activate(pin):
    GPIO.output(pin, GPIO.HIGH)

def deactivate(pin):
    GPIO.output(pin, GPIO.LOW)
