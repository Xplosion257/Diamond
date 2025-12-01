"""
The date module of time and frames
"""
import time

# Time since Unix Epoch
def time_secs():
    return time.time()

# Date in a readable format
def date():
    return time.ctime()

# Delta time
def delta(last_frame: float) -> float:
    current_frame = time.time()
    delta_time = round(current_frame - last_frame, 4)
    return delta_time

# FPS
def fps(delta_time: float) -> float:
    if delta_time == 0:
        raise ZeroDivisionError("delta time is 0, it is impossible to calulate framerate from that")
    return 1.0 / delta_time

# Timer
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time
        duration = round(end - start, 4)
        return duration
    return wrapper
