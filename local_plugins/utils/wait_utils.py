import threading



class ThreadWait:

    @staticmethod
    def wait(time_to_wait):
        sleep_event = threading.Event()
        sleep_event.wait(time_to_wait)
        sleep_event.set()

    @staticmethod
    def sleep(time_to_sleep):
        import time
        time.sleep(time_to_sleep)
