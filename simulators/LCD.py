import time
import threading

class LCDSimulator:

    def __init__(self):
        self.current_text = ""
        self.lock = threading.Lock()

        t = threading.Thread(target=self._loop, daemon=True)
        t.start()

    def set_text(self, text):
        with self.lock:
            self.current_text = text

    def _loop(self):
        while True:
            with self.lock:
                print("LCD DISPLAY:")
                print(self.current_text)
                print("------------------")
            time.sleep(3)