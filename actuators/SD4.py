import threading
import RPi.GPIO as GPIO
import time

class SD4Controller:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.segments = (11,4,23,8,7,10,18,25)
        self.digits = (22,27,17,24)

        for s in self.segments:
            GPIO.setup(s, GPIO.OUT)
            GPIO.output(s, 0)

        for d in self.digits:
            GPIO.setup(d, GPIO.OUT)
            GPIO.output(d, 1)

        self.num = {
            '0':(1,1,1,1,1,1,0),
            '1':(0,1,1,0,0,0,0),
            '2':(1,1,0,1,1,0,1),
            '3':(1,1,1,1,0,0,1),
            '4':(0,1,1,0,0,1,1),
            '5':(1,0,1,1,0,1,1),
            '6':(1,0,1,1,1,1,1),
            '7':(1,1,1,0,0,0,0),
            '8':(1,1,1,1,1,1,1),
            '9':(1,1,1,1,0,1,1),
            ' ':(0,0,0,0,0,0,0)
        }

        self.current_time = "00:00"
        self.lock = threading.Lock()

        thread = threading.Thread(target=self._display_loop, daemon=True)
        thread.start()

    def set_time(self, time_string):
        with self.lock:
            self.current_time = time_string

    def _display_loop(self):

        while True:

            with self.lock:
                t = self.current_time

            for digit in range(5):
                if digit==2:
                    continue
                for loop in range(0,7):
                    GPIO.output(self.segments[loop], self.num[t[digit]][loop])
                
                GPIO.output(self.digits[digit], 0)
                time.sleep(0.001)
                GPIO.output(self.digits[digit], 1)
                
