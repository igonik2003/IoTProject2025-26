import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def setup(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def on(pin):
    GPIO.output(pin, GPIO.HIGH)

def off(pin):
    GPIO.output(pin, GPIO.LOW)

def cleanup():
    GPIO.cleanup()
