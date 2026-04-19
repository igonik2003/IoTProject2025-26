import time
import random
    
def run_ds2_simulator(delay,callback,stop_event):
    button_pressed = False
    hold_cycles_remaining = 0

    while not stop_event.is_set():

        if hold_cycles_remaining > 0:
            # Dugme je već pritisnuto i treba da ostane pritisnuto
            hold_cycles_remaining -= 1

        else:
            # Odlučujemo da li da započnemo novo držanje
            if random.randint(0, 3) == 1:   # ~20% šanse da počne držanje
                button_pressed = True

                # Drži dugme 3–6 ciklusa
                hold_cycles_remaining = random.randint(3, 6)

            else:
                button_pressed = False
        
        print("Button pressed ", button_pressed)
        callback(button_pressed)
        time.sleep(delay)