import threading
from simulators.IR import run_ir_simulator

def run_ir(settings, data_queue, threads, stop_event, brgb_controller):

    def ir_callback(r,g,b):
        brgb_controller(r,g,b)

        data_queue.put((
            "iot/pi3/ir",
            {
                "value": f"{r},{g},{b}",
                "simulated": settings["simulated"]
            }
        ))

    t = threading.Thread(
        target=run_ir_simulator,
        args=(5, ir_callback, stop_event),
        daemon=True
    )

    t.start()
    threads.append(t)