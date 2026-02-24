import RPi.GPIO as GPIO

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


def on():
    GPIO.output(LED_PIN, GPIO.HIGH)


def off():
    GPIO.output(LED_PIN, GPIO.LOW)
