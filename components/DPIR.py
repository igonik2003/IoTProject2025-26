#from sensors.DPIR1 import run_dpir1_loop
from simulators.DPIR1 import run_dpir1_simulator
import threading
import time

def run_dpir1(settings, threads, stop_event):
        if settings['simulated']==True:
            dpir1_thread = threading.Thread(target = run_dpir1_simulator, args=(2,stop_event))
            print("Dpir1 sumilator started")
            dpir1_thread.start()
            threads.append(dpir1_thread)
        else:
            """
            dpir1_thread = threading.Thread(target=run_dpir1_loop, args=(2,stop_event))
            print("Dpir1 loop started")    
            dpir1_thread.start()
            threads.append(dpir1_thread)
            """
            print("Real sensor implementation.")   