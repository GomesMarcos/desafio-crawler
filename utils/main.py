from time import time


URL_IMDB = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


def time_delta(func):

    def wrapper(*args, **kwargs):
        start_time = time()
        execution = func(*args, **kwargs)
        end_time = time()
        time_delta = end_time - start_time
        return execution, time_delta

    return wrapper