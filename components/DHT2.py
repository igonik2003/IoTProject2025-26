from simulators.DHT2 import run_dht2_simulator
from sensors.DHT2 import run_dht2_loop
import threading

def run_dht2(settings, data_queue, threads, stop_event, lcd_manager):

    def dht2_callback(temperature, humidity):
        lcd_manager.update("dht2", temperature, humidity)
        data_queue.put((
            "iot/pi3/dht2/temperature",
            {
                "value": temperature,
                "simulated": settings["simulated"]
            }
        ))

        data_queue.put((
            "iot/pi3/dht2/humidity",
            {
                "value": humidity,
                "simulated": settings["simulated"]
            }
        ))

    if settings["simulated"]:

        t = threading.Thread(
            target=run_dht2_simulator,
            args=(2, dht2_callback, stop_event),
            daemon=True
        )
        print("DHT2 simulator started")

    else:

        pin = settings["pin"]

        t = threading.Thread(
            target=run_dht2_loop,
            args=(2, dht2_callback, stop_event, pin),
            daemon=True
        )
        print("DHT2 real sensor started")

    t.start()
    threads.append(t)