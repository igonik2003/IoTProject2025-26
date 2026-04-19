import threading
import time


class SecurityAlarmController:

    def __init__(self, settings,data_queue, db_activate, db_deactivate):
        self.data_queue = data_queue
        self.db_activate = db_activate
        self.db_deactivate = db_deactivate
        self.settings=settings
        self.people_count = 0
        self.alarm_active = False
        self.lock = threading.Lock()

    # Poziva PeopleCounterController kada se broj promeni
    def update_people_count(self, count):
        with self.lock:
            self.people_count = count

            # AUTOMATSKO GAŠENJE
            if self.alarm_active and self.people_count > 0:
                self._deactivate_alarm()

    # Poziva DPIR senzor kada detektuje pokret
    def motion_detected(self):
        with self.lock:

            if self.people_count == 0 and not self.alarm_active:
                self._activate_alarm()

    def _activate_alarm(self):
        self.alarm_active = True
        print("SECURITY ALARM ACTIVATED")

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
        print("SECURITY ALARM DEACTIVATED")
        
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