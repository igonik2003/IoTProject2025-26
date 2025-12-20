#from sensors.DUS1 import run_dus1_loop
from simulators.DUS1 import run_dus1_simulator
import threading
import time

def dus1_callback(distance):
    print(f"Distance: {distance}")

def run_dus1(settings, threads, stop_event):
        if settings['simulated']==True:
            dus1_thread = threading.Thread(target = run_dus1_simulator, args=(2, dus1_callback, stop_event))
            dus1_thread.start()
            threads.append(dus1_thread)
            print("Dus1 sumilator started")
        else:
            """
            dus1_thread = threading.Thread(target=run_dus1_loop, args=(2, dus1_callback, stop_event))
            dus1_thread.start()
            threads.append(dus1_thread)
            print("Dus1 loop started")    
            """
            print("Real sensor implementation.")        
