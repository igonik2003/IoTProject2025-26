try:
    import Adafruit_DHT
except ImportError:
    Adafruit_DHT = None
import time

if Adafruit_DHT:

    DHT_SENSOR = Adafruit_DHT.DHT11

    def run_dht1_loop(delay, callback, stop_event, pin):
        import time
        while not stop_event.is_set():
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, pin)
            if humidity and temperature:
                callback(temperature, humidity)
            time.sleep(delay)

else:
    def run_dht1_loop(delay, callback, stop_event, pin):
        print("DHT1 real sensor not available")