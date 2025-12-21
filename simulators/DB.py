import time

def beep(pin, duration=1):
    print(f"[SIM] Buzzer ON for {duration}s")
    time.sleep(duration)
    print("[SIM] Buzzer OFF")
