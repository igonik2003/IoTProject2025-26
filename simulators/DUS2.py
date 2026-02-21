import time
import random

def generate_values(initial_distance=200):
    distance = initial_distance

    mode = "idle"      # idle, approaching, leaving
    steps_remaining = 0

    while True:

        # Ako nismo u pokretu, postoji šansa da započnemo kretanje
        if mode == "idle":
            if random.random() < 0.9:  # 10% šanse da počne događaj
                mode = random.choice(["approaching", "leaving"])
                steps_remaining = random.randint(5, 8)

        # Ako se osoba približava
        if mode == "approaching":
            distance -= random.randint(15, 30)
            steps_remaining -= 1

            if steps_remaining <= 0:
                mode = "idle"

        # Ako se osoba udaljava
        elif mode == "leaving":
            distance += random.randint(15, 30)
            steps_remaining -= 1

            if steps_remaining <= 0:
                mode = "idle"

        # Idle režim – mali šum
        else:
            distance += random.randint(-2, 2)

        # Ograničenja
        if distance < 5:
            distance = 5
        if distance > 400:
            distance = 400

        yield distance
     

def run_dus2_simulator(delay, callback, stop_event):
        for d in generate_values():
            time.sleep(delay) 
            callback(d)
            if stop_event.is_set():
                  break