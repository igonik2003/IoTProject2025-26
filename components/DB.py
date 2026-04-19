import threading

def run_db(settings, data_queue, threads, stop_event):

    if settings["simulated"]==False:
        """from actuators.DB import setup, on, off

        DB_PIN = 20  # ili iz settings.json
        setup(DB_PIN)

        def activate():
            on(DB_PIN)
            data_queue.put((
                "iot/pi1/db",
                {
                    "value": 1,
                    "simulated": False
                }
            ))

        def deactivate():
            off(DB_PIN)
            data_queue.put((
                "iot/pi1/db",
                {
                    "value": 0,
                    "simulated": False
                }
            ))

        return activate, deactivate"""
        return None,None
    
    else:
        return None,None
