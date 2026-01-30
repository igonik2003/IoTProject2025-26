import queue
import json
import time

def mqtt_publisher_loop(mqtt_client, data_queue, stop_event, batch_size=5):
    batch = []

    while not stop_event.is_set():
        try:
            item = data_queue.get(timeout=1)
            batch.append(item)
            data_queue.task_done()

            if len(batch) >= batch_size:
                for topic, payload in batch:
                    mqtt_client.publish(topic, json.dumps(payload))
                batch.clear()

        except queue.Empty:
            if batch:
                for topic, payload in batch:
                    mqtt_client.publish(topic, json.dumps(payload))
                batch.clear()