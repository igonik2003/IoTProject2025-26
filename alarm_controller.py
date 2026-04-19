import time
import threading

class AlarmController:

    def __init__(self,settings,data_queue, db_activate_callback, db_deactivate_callback):
        self.data_queue = data_queue

        self.db_activate = db_activate_callback
        self.db_deactivate = db_deactivate_callback
        self.settings=settings
        self.ds1_pressed_since = None
        self.ds2_pressed_since = None

        self.alarm_active = False
        self.lock = threading.Lock()

    def process_ds1(self, state: bool):
        self._process_sensor("ds1", state)

    def process_ds2(self, state: bool):
        self._process_sensor("ds2", state)

    def _process_sensor(self, sensor_name, state):

        with self.lock:
            now = time.time()

            if sensor_name == "ds1":
                pressed_since = self.ds1_pressed_since
            else:
                pressed_since = self.ds2_pressed_since

            # Ako je dugme pritisnuto
            if state:
                if pressed_since is None:
                    if sensor_name == "ds1":
                        self.ds1_pressed_since = now
                    else:
                        self.ds2_pressed_since = now
                else:
                    # Provera da li je 5 sekundi prošlo
                    if not self.alarm_active and now - pressed_since >= 5:
                        self._activate_alarm()

            # Ako je dugme pušteno
            else:
                if sensor_name == "ds1":
                    self.ds1_pressed_since = None
                else:
                    self.ds2_pressed_since = None

                if self.alarm_active:
                    self._deactivate_alarm()

    def _activate_alarm(self):
        self.alarm_active = True
        print("ALARM ACTIVATED")

        if(self.settings==False):
            self.db_activate()
        else:
            self.data_queue.put((
                "iot/pi1/db",
                {
                    "value": int(True),
                    "simulated": True
                }
            ))    

        self.data_queue.put((
            "iot/house/alarm",
            {
                "value": 1,
                "simulated": self.settings
            }
        ))

    def _deactivate_alarm(self):
        self.alarm_active = False
        print("ALARM DEACTIVATED")
        
        if(self.settings==False):
            self.db_deactivate()
        else:
            self.data_queue.put((
                "iot/pi1/db",
                {
                    "value": int(False),
                    "simulated": True
                }
            ))   

        self.data_queue.put((
            "iot/house/alarm",
            {
                "value": 0,
                "simulated": self.settings
            }
        ))