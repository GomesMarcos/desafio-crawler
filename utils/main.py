from time import time


URL_IMDB = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
SCREENSHOT_FILENAME = "movies.png"
JSON_FILENAME = "movies.json"
SAVING_PLACES = ["db", "json"]


def time_delta(func):

    def wrapper(*args, **kwargs):
        start_time = time()
        execution = func(*args, **kwargs)
        end_time = time()
        time_delta = end_time - start_time
        return execution, time_delta

    return wrapper


def remove_files_if_exists():
    import os
    for file in [SCREENSHOT_FILENAME, JSON_FILENAME]:
        if os.path.exists(file):
            os.remove(file)
