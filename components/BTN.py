#from sensors.BTN import run_btn_loop
from simulators.BTN import run_btn_simulator
import threading
import time     

def run_btn(settings,data_queue, threads, stop_event):
    def btn_callback(button_pressed: bool):
        data_queue.put((
            "iot/pi2/btn",
            {
                "value": button_pressed,
                "simulated": settings["simulated"],
            }
        ))
    if settings['simulated']==True:
        btn_thread = threading.Thread(target = run_btn_simulator, args=(2,btn_callback,stop_event))
        print("Btn sumilator started")
        btn_thread.start()
        threads.append(btn_thread)
    else:
        """
        btn_thread = threading.Thread(target=run_btn_loop, args=(2,btn_callback,stop_event))
        print("Btn loop started")    
        btn_thread.start()
        threads.append(btn_thread)
        """
        print("Real sensor implementation.")          