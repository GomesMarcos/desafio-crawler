import sys
from time import sleep

from selenium.webdriver import Firefox, FirefoxOptions


sys.path.append(".")

from utils import (
    URL_IMDB,
    get_all_movies,
    get_movie_info,
    log_except,
    log_message,
    time_delta,
)


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
        try:
            log_message("saving movies information")
            with open('../movies.json', 'w') as file:
                while movies:
                    movie = get_movie_info(next(movies))
                    file.write(f"{movie}\n")
                    print(f'\033[93m\n\nmovie: {movie} \n\n\033[0m')
        except StopIteration:
            log_message("All movies are successfully")


if __name__ == "__main__":
    ws = WebScrapper()
    movies = ws.scrap_url()
    print(movies)
