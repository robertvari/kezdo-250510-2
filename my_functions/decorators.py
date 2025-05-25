import time
from datetime import datetime

def my_timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)
        
        stop_time = time.time()
        print(f"Process time: {stop_time-start_time}")
        return result
    return wrapper

def time_logger(func):
    def wrapper(*args, **qwargs):
        print(f"Function called: {datetime.now()}")
        result = func(*args, **qwargs)
        return result
    return wrapper