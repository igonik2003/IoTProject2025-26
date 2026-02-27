from simulators.DHT1 import run_dht1_simulator
from sensors.DHT1 import run_dht1_loop
from components.LCD import LCDManager
import threading

def run_dht1(settings, data_queue, threads, stop_event, lcd_manager):

    def dht1_callback(temperature, humidity):
        lcd_manager.update("dht1", temperature, humidity)
        data_queue.put((
            "iot/pi3/dht1/temperature",
            {
                "value": temperature,
                "simulated": settings["simulated"]
            }
        ))

        data_queue.put((
            "iot/pi3/dht1/humidity",
            {
                "value": humidity,
                "simulated": settings["simulated"]
            }
        ))

    if settings["simulated"]:

        t = threading.Thread(
            target=run_dht1_simulator,
            args=(2, dht1_callback, stop_event),
            daemon=True
        )
        print("DHT1 simulator started")

    else:

        pin = settings["pin"]

        t = threading.Thread(
            target=run_dht1_loop,
            args=(2, dht1_callback, stop_event, pin),
            daemon=True
        )
        print("DHT1 real sensor started")

    t.start()
    threads.append(t)