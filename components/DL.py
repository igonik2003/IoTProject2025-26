import threading
#from actuators.DL import run_dl_loop
from simulators.DL import run_dl_simulator

def run_dl(settings, data_queue, threads, stop_event):

    def dl_callback(state: int):
        data_queue.put((
            "iot/pi1/dl",
            {
                "value": state,
                "simulated": settings["simulated"]
            }
        ))

    #t = threading.Thread(
     #   target=run_dl_simulator,
      #  args=(2, dl_callback, stop_event),
     #   daemon=True
    #)
    #t.start()
    #threads.append(t)
    
    if settings['simulated']==True:
            dl_thread = threading.Thread(target = run_dl_simulator, args=(2,dl_callback,stop_event))
            print("Dl sumilator started")
            dl_thread.start()
            threads.append(dl_thread)
    else:
        """
        dl_thread = threading.Thread(target=run_dl_loop, args=(2,dl_callback,stop_event))
        print("Dl loop started")    
        dl_thread.start()
        threads.append(dl_thread)
        """
        print("Real sensor implementation.")