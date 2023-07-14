import sys


sys.path.append(".")
from Db.main import DbConn
from Db.movie import query_create_table_movie, query_save_movie
from utils import get_movie_info, log_except, log_message


def save_movies_into_db(movies):
    log_message("Start saving movies into DB")
    try:
        conn = DbConn()
        conn.execute_and_commit_query(query_create_table_movie())
        while movies:
            movie = get_movie_info(next(movies))
            query = query_save_movie(movie)
            conn.execute_and_commit_query(query)
        log_message("Movies saved into DB successfully")
        conn.close()
    except Exception as e:
        log_except(e)
