import threading

def run_sensor(sensor_code, simulator_fn, settings, data_queue, stop_event):
    topic_base = settings["mqtt"]["base_topic"]
    pi_id = settings["device"]["pi_id"]
    sensor_settings = settings["sensors"][sensor_code]

    def callback(value):
        data_queue.put((
            f"{topic_base}/{sensor_code.lower()}",
            {
                "value": value,
                "simulated": sensor_settings["simulated"],
                "pi_id": pi_id,
                "sensor": sensor_code
            }
        ))

    t = threading.Thread(
        target=simulator_fn,
        args=(2, callback, stop_event),
        daemon=True
    )
    t.start()
    return t
