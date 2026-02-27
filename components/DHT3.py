from simulators.DHT3 import run_dht3_simulator
from sensors.DHT3 import run_dht3_loop
import threading

def run_dht3(settings, data_queue, threads, stop_event):

    def dht3_callback(temperature, humidity):

        data_queue.put((
            "iot/pi2/dht3/temperature",
            {
                "value": temperature,
                "simulated": settings["simulated"]
            }
        ))

        data_queue.put((
            "iot/pi2/dht3/humidity",
            {
                "value": humidity,
                "simulated": settings["simulated"]
            }
        ))

    if settings["simulated"]:

        t = threading.Thread(
            target=run_dht3_simulator,
            args=(2, dht3_callback, stop_event),
            daemon=True
        )
        print("DHT3 simulator started")

    else:

        pin = settings["pin"]

        t = threading.Thread(
            target=run_dht3_loop,
            args=(2, dht3_callback, stop_event, pin),
            daemon=True
        )
        print("DHT3 real sensor started")

    t.start()
    threads.append(t)