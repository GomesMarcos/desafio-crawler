from time import time


URL_IMDB = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
SCREENSHOT_FILENAME = "movies.png"
JSON_FILENAME = "movies.json"
DB_FILENAME = "db.sqlite3"
SAVING_PLACES = ["db", "json"]


def time_delta(func):

    def wrapper(*args, **kwargs):
        start_time = time()
        execution = func(*args, **kwargs)
        end_time = time()
        time_delta = end_time - start_time
        log_time_delta(time_delta)
        return execution

    return wrapper


def remove_files_if_exists():
    import os
    for file in [SCREENSHOT_FILENAME, JSON_FILENAME, DB_FILENAME]:
        if os.path.exists(file):
            os.remove(file)


def log_time_delta(time_delta):
    quick = time_delta < 20
    mid = time_delta >= 20 and time_delta <= 40
    message = f'A execução demorou {time_delta} segundos'

    if quick:
        print(f'\033[92m\n\n{message}\n\n\033[0m')
    elif mid:
        print(f'\033[93m\n\n{message}\n\n\033[0m')
    else:
        print(f'\033[91m\n\n{message}\n\n\033[0m')
