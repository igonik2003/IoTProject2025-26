import threading
import time

class PinController:

    def __init__(self, security_controller, data_queue):
        self.security_controller = security_controller
        self.data_queue = data_queue
        self.correct_pin = "1234"
        self.buffer = ""
        self.system_armed = False

    def enter_digit(self, digit):

        self.buffer += str(digit)

        if len(self.buffer) == 4:

            if self.buffer == self.correct_pin:

                if not self.system_armed:
                    print("Correct PIN - arming in 10 seconds")
                    threading.Thread(
                        target=self._arm_delay,
                        daemon=True
                    ).start()
                else:
                    print("Correct PIN - disarming")
                    self.system_armed = False
                    self.security_controller._deactivate_alarm()

                    self.data_queue.put((
                        "iot/house/system_armed",
                        {
                            "value": 0,
                            "simulated": True
                        }
                    ))

            else:
                print("Wrong PIN")

            self.buffer = ""

    def _arm_delay(self):
        time.sleep(10)
        self.system_armed = True
        print("System armed")

        self.data_queue.put((
            "iot/house/system_armed",
            {
                "value": 1,
                "simulated": True
            }
        ))