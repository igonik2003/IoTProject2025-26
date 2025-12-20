#from sensors.DUS1 import run_dus1_loop
#from sensors.DPIR1 import run_dpir1_loop
from simulators.DUS1 import run_dus1_simulator
from simulators.DPIR1 import run_dpir1_simulator
import threading
import time

def dus1_callback(distance):
    print(f"[{time.strftime('%H:%M:%S')}] Distance: {distance}")

def run_dus1(settings, threads, stop_event):
        if settings['simulated']==True:
            dus1_thread = threading.Thread(target = run_dus1_simulator, args=(2, dus1_callback, stop_event))
            print("Dus1 sumilator started")
            dus1_thread.start()
            threads.append(dus1_thread)
        else:
            """
            dus1_thread = threading.Thread(target=run_dus1_loop, args=(2, dus1_callback, stop_event))
            dus1_thread.start()
            threads.append(dus1_thread)
            print("Dus1 loop started")    
            """
            print("Real sensor implementation.")        

def run_dpir1(settings, threads, stop_event):
        if settings['simulated']==True:
            dpir1_thread = threading.Thread(target = run_dpir1_simulator, args=(2,stop_event))
            print("Dpir1 sumilator started")
            dpir1_thread.start()
            threads.append(dpir1_thread)
        else:
            """
            dpir1_thread = threading.Thread(target=run_dpir1_loop, args=(2,stop_event))
            dpir1_thread.start()
            threads.append(dpir1_thread)
            print("Dpir1 loop started")    
            """
            print("Real sensor implementation.")            
