import queue
import json
import time

def mqtt_publisher_loop(mqtt_client, data_queue, stop_event, settings):
    batch = []
    batch_size = settings["batch"]["size"]
    interval = settings["batch"]["interval_sec"]
    last_send = time.time()

    while not stop_event.is_set():
        try:
            item = data_queue.get(timeout=1)
            batch.append(item)
            data_queue.task_done()
        except queue.Empty:
            pass

        if len(batch) >= batch_size or (time.time() - last_send) >= interval:
            for topic, payload in batch:
                mqtt_client.publish(topic, json.dumps(payload))
            batch.clear()
            last_send = time.time()
