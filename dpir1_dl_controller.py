import threading


class DpirDlController:
    def __init__(self, dl_turn_on, dl_turn_off, publish_callback):
        """
        :param dl_turn_on: funkcija za paljenje LED (real ili simulacija)
        :param dl_turn_off: funkcija za gašenje LED
        :param publish_callback: funkcija za slanje stanja LED u queue (MQTT, baza itd.)
        """

        self.dl_turn_on = dl_turn_on
        self.dl_turn_off = dl_turn_off
        self.publish_callback = publish_callback

        self.lock = threading.Lock()
        self.timer = None
        self.led_is_on = False

    def motion_detected(self):
        """
        Poziva se kada PIR detektuje pokret.
        """
        with self.lock:
            # Ako LED nije upaljena → upali je
            if not self.led_is_on:
                self.dl_turn_on()
                self.publish_callback(1)
                self.led_is_on = True

            # Ako već postoji timer → resetuj ga
            if self.timer:
                self.timer.cancel()

            # Pokreni novi timer od 10 sekundi
            self.timer = threading.Timer(10, self.turn_off_led)
            self.timer.start()

    def turn_off_led(self):
        """
        Gasi LED kada istekne 10 sekundi bez novog pokreta.
        """

        with self.lock:
            self.dl_turn_off()
            self.publish_callback(0)
            self.led_is_on = False
            self.timer = None