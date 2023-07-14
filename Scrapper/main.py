import sys
from time import sleep

from selenium.webdriver import Firefox, FirefoxOptions


sys.path.append(".")

from Db.main import DbConn
from utils import (
    SAVING_PLACES,
    URL_IMDB,
    get_all_movies,
    get_movie_info,
    log_except,
    log_message,
    prepare_ending_json_file,
    remove_files_if_exists,
    save_movie_into_json,
    time_delta,
)
from utils.db import save_movie_into_db


class WebScrapper:
    """
    Class for handling web scrapping
    """

    def __init__(self, url=""):
        self.url = url or URL_IMDB
        self.options = self._set_options()
        self.driver = Firefox(options=self.options)
        self.waiting_seconds = 2

    @time_delta
    def scrap_url(self):
        try:
            log_message(f"browsering {URL_IMDB}")
            self.driver.get(URL_IMDB)

            log_message("parsing content")
            sleep(self.waiting_seconds)

            movies = get_all_movies(self.driver)
            self._save_movies(movies)

            log_message("closing browser")
            self.driver.close()

        except Exception as e:
            log_except(e)

    def _set_options(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        return options

    @staticmethod
    def _save_movies(movies):
        movie_count = 0
        conn = DbConn()
        try:
            while movies:
                movie = get_movie_info(next(movies))
                if "json".lower() in SAVING_PLACES:
                    save_movie_into_json(movie, is_start=movie_count == 0)
                if "db".lower() in SAVING_PLACES:
                    save_movie_into_db(movie, conn)
                else:
                    conn.close()
                movie_count += 1
        except StopIteration:
            if "json".lower() in SAVING_PLACES:
                save_movie_into_json(movie, is_end=True)
            if "db".lower() in SAVING_PLACES:
                save_movie_into_db(movie, conn, is_end=True)


if __name__ == "__main__":
    remove_files_if_exists()
    ws = WebScrapper()
    movies = ws.scrap_url()
    print(movies)
