try:
    import Adafruit_DHT
except ImportError:
    Adafruit_DHT = None
import time

try:
    import Adafruit_DHT
except ImportError:
    Adafruit_DHT = None


if Adafruit_DHT:
    DHT_SENSOR = Adafruit_DHT.DHT11

    def run_dht3_loop(delay, callback, stop_event, pin):
        import time

        while not stop_event.is_set():
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, pin)

            if humidity is not None and temperature is not None:
                callback(temperature, humidity)

            time.sleep(delay)
else:
    # Dummy funkcija za Windows
    def run_dht3_loop(delay, callback, stop_event, pin):
        print("DHT3 real sensor not available on this system")

def run_dht3_loop(delay, callback, stop_event, pin):

    while not stop_event.is_set():

        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, pin)

        if humidity is not None and temperature is not None:
            callback(round(temperature,2), round(humidity,2))
        else:
            print("DHT3 read failed")

        time.sleep(delay)