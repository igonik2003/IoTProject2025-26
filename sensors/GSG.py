try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None


if GPIO:

    import time

    GPIO.setmode(GPIO.BCM)
    GSG_PIN = 25

    GPIO.setup(GSG_PIN, GPIO.IN)

    def run_gsg_loop(delay, callback, stop_event):
        while not stop_event.is_set():
            state = GPIO.input(GSG_PIN)
            callback(state)
            time.sleep(delay)

else:
    # Dummy funkcija za Windows
    def run_gsg_loop(delay, callback, stop_event):
        print("GSG real sensor not available on this system")

def run_gsg_loop(delay, callback, stop_event, pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

    while not stop_event.is_set():

        movement = GPIO.input(pin)

        callback(bool(movement))

        time.sleep(delay)