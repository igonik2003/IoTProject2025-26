try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None


class BRGBController:

    def __init__(self, r_pin, g_pin, b_pin):
        if GPIO is None:
            raise RuntimeError("GPIO not available")

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(r_pin, GPIO.OUT)
        GPIO.setup(g_pin, GPIO.OUT)
        GPIO.setup(b_pin, GPIO.OUT)

        self.r = GPIO.PWM(r_pin, 100)
        self.g = GPIO.PWM(g_pin, 100)
        self.b = GPIO.PWM(b_pin, 100)

        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    def set_color(self, r, g, b):
        self.r.ChangeDutyCycle(r)
        self.g.ChangeDutyCycle(g)
        self.b.ChangeDutyCycle(b)