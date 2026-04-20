import threading
from simulators.BRGB import set_color as sim_set_color

def run_brgb(settings, data_queue, threads, stop_event):

    def publish_color(r, g, b):
        data_queue.put((
            "iot/pi3/brgb/state",
            {
                "value": f"{r},{g},{b}",
                "simulated": settings["simulated"]
            }
        ))

    if settings["simulated"]:
        def controller(r, g, b):
            sim_set_color(r, g, b)
            publish_color(r, g, b)
    else:
        from actuators.BRGB import BRGBController
        ctrl = BRGBController(12, 13, 19)  # primer pinova

        def controller(r, g, b):
            ctrl.set_color(r, g, b)
            publish_color(r, g, b)

    return controller