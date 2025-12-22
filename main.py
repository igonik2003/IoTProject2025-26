import threading
from settings import load_settings
from components.DUS1 import run_dus1
from components.DPIR import run_dpir1
from components.DS1 import run_ds1
from components.DL import run_dl
from components.DB import run_db
from components.DMS import run_dms


import time

if __name__ == "__main__":
    print('Starting app')
    settings = load_settings()
    threads = []
    stop_event = threading.Event()
    try:
        dus1_settings = settings['DUS1']
        run_dus1(dus1_settings, threads, stop_event)
        dpir1_settings = settings['DPIR1']
        run_dpir1(dpir1_settings, threads, stop_event)
        ds1_settings = settings['DS1']
        run_ds1(ds1_settings, threads, stop_event)
        dl_settings = settings["DL"]
        run_dl(dl_settings, threads, stop_event)
        db_settings = settings["DB"]
        run_db(db_settings, threads, stop_event)
        dms_settings = settings["DMS"]
        run_dms(dms_settings, threads, stop_event)
        while True:
            time.sleep(5)

    except KeyboardInterrupt:
        for t in threads:
            stop_event.set()
