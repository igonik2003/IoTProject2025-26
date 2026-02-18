import threading
from dpir1_dl_controller import DpirDlController
import datetime 

# REAL ILI SIM LED
#from actuators.DL import on as real_on, off as real_off
from simulators.DL import on as sim_on, off as sim_off

# PIR senzori
# from sensors.DPIR1 import run_dpir1_loop
from simulators.DPIR1 import run_dpir1_simulator


def run_dpir1(settings,data_queue, threads, stop_event):

    # Funkcija za slanje stanja LED
    def publish_led_state(state):
        data_queue.put((
            "iot/pi1/dl",
            {
                "value": state,
                "simulated": settings["simulated"]
            }
        ))

    # Kreiranje controller-a (real ili simulacija)
    if settings["simulated"]:
        controller = DpirDlController(sim_on, sim_off, publish_led_state)
        publish_led_state(0)
        print(datetime.datetime.now())
    else:
        #controller = DpirDlController(real_on, real_off, publish_led_state)
        print("Real")

    # Callback kada PIR detektuje pokret
    def dpir1_callback(motion_detected: bool):
        # šaljemo stanje PIR senzora
        data_queue.put((
            "iot/pi1/dpir1",
            {
                "value": motion_detected,
                "simulated": settings["simulated"],
            }
        ))

        # ako je detektovan pokret → obavesti controller
        if motion_detected:
            controller.motion_detected()

    # Pokretanje odgovarajućeg PIR-a
    if settings["simulated"]:
        dpir1_thread = threading.Thread(
            target=run_dpir1_simulator,
            args=(2,dpir1_callback, stop_event)
        )
        print("DPIR1 simulator started")
    else:
        #dpir1_thread = threading.Thread(
           # target=run_dpir1_loop,
           # args=(2,dpir1_callback, stop_event)
        #)
        print("DPIR1 real sensor started")

    dpir1_thread.start()
    threads.append(dpir1_thread)