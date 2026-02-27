try:
    import Adafruit_DHT
except ImportError:
    Adafruit_DHT = None

import time


if Adafruit_DHT:

    DHT_SENSOR = Adafruit_DHT.DHT11

    def run_dht2_loop(delay, callback, stop_event, pin):

        while not stop_event.is_set():

            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, pin)

            if humidity is not None and temperature is not None:
                callback(round(temperature,2), round(humidity,2))
            else:
                print("DHT2 read failed")

            time.sleep(delay)

else:
    def run_dht2_loop(delay, callback, stop_event, pin):
        print("DHT2 real sensor not available on this system")