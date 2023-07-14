import sys


sys.path.append(".")
from Db.movie import query_save_movie
from utils import log_except, log_message


def save_movie_into_db(movie, conn, is_end=False):
    try:
        if is_end:
            log_message("All movies saved on DB successfully")
            return conn.close()
        query = query_save_movie(movie)
        conn.execute_and_commit_query(query)
    except Exception as e:
        log_except(e)
