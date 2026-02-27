try:
    from RPLCD.i2c import CharLCD
except ImportError:
    CharLCD = None


if CharLCD:

    class LCDController:

        def __init__(self):
            self.lcd = CharLCD(
                i2c_expander='PCF8574',
                address=0x27,
                port=1,
                cols=16,
                rows=2
            )

        def display(self, line1, line2):
            self.lcd.clear()
            self.lcd.write_string(line1 + "\n" + line2)

else:

    class LCDController:

        def __init__(self):
            print("LCD real hardware not available")

        def display(self, line1, line2):
            print(f"LCD SIM -> {line1} | {line2}")