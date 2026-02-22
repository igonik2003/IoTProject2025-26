import threading
import time


class TimerController:

    def __init__(self, publish_display):
        self.publish_display = publish_display
        self.current_seconds = 0
        self.add_seconds = 0
        self.blinking = False
        self.running = False
        self.lock = threading.Lock()

    def set_settings(self, seconds):
        with self.lock:
            self.current_seconds = seconds
            self.running = True
            self.blinking = False

    def set_settings1(self,add_seconds):
        with self.lock:
            self.add_seconds = add_seconds

    def button_pressed(self):
        with self.lock:

            if self.blinking:
                self.blinking = False
                self.running = False
                return

            if self.running:
                self.current_seconds += self.add_seconds

    def start(self):
        thread = threading.Thread(target=self._run)
        thread.daemon = True
        thread.start()

    def _run(self):
        while True:
            time.sleep(2)

            with self.lock:

                print(self.format_time())
                if not self.running:
                    continue

                if self.current_seconds > 0:
                    self.current_seconds -= 1
                    self.publish_display(self.format_time())

                else:
                    self.running = False
                    self.blinking = True

            if self.blinking:
                self._blink()

    def _blink(self):
        while self.blinking:
            self.publish_display("00:00")
            time.sleep(0.5)
            self.publish_display("    ")
            time.sleep(0.5)

    def format_time(self):
        minutes = self.current_seconds // 60
        seconds = self.current_seconds % 60
        return f"{minutes:02}:{seconds:02}"