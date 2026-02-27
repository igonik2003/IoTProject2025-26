import threading
import time

from simulators.LCD import LCDSimulator
from actuators.LCD import LCDController

class LCDManager:

    def __init__(self, settings):

        self.simulated = settings["simulated"]

        if self.simulated:
            self.display = LCDSimulator()
        else:
            self.display = LCDController()

        self.values = {
            "dht1": None,
            "dht2": None,
            "dht3": None
        }

        t = threading.Thread(target=self._rotation_loop, daemon=True)
        t.start()

    def update(self, sensor_name, temperature, humidity):
        self.values[sensor_name] = (temperature, humidity)

    def _rotation_loop(self):
        sensors = ["dht1", "dht2", "dht3"]
        index = 0

        while True:
            sensor = sensors[index]
            data = self.values.get(sensor)

            if data:
                t, h = data
                text = f"{sensor.upper()}\nT:{t}C H:{h}%"
                self.display.set_text(text)

            index = (index + 1) % 3
            time.sleep(4)