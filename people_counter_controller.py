import threading
from collections import deque


class PeopleCounterController:

    def __init__(self, publish_callback,security_controller, history_size=5):
        self.publish_callback = publish_callback
        self.security_controller = security_controller
        self.history = deque(maxlen=history_size)
        self.people_count = 0
        self.lock = threading.Lock()

    # DUS1 šalje distance ovde
    def add_distance(self, distance):
        with self.lock:
            self.history.append(distance)

    # DPIR1 okida analizu
    def motion_triggered(self):
        with self.lock:

            # Mora imati bar 5 merenja
            if len(self.history) < 5:
                return

            # Uzmi tačno poslednjih 5
            distances = list(self.history)[-5:]

            # Proveri da li je strogo opadajuće
            strictly_decreasing = all(
                distances[i+1] < distances[i]
                for i in range(len(distances) - 1)
            )

            # Proveri da li je strogo rastuće
            strictly_increasing = all(
                distances[i+1] > distances[i]
                for i in range(len(distances) - 1)
            )

            if strictly_decreasing:
                # osoba se približava → ulazi
                self.people_count += 1
                direction = "IN"

            elif strictly_increasing:
                # osoba se udaljava → izlazi
                self.people_count = max(0, self.people_count - 1)
                direction = "OUT"

            else:
                # nema čistog trenda
                return

            #print("Last 5 distances:", distances)
            #print("Direction:", direction, "People:", self.people_count)
            self.publish_callback(self.people_count)
            self.security_controller.update_people_count(self.people_count)
