from logging import getLevelNamesMapping, log
from time import sleep, time

from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
LOG_LEVELS = getLevelNamesMapping()


class WebScrapper:
    """
    Class for handling web scrapping
    """

    def __init__(self, url=""):
        self.url = url or URL
        self.options = self._set_options()
        self.browser = Firefox(options=self.options)

    def scrap_url(self):
        try:
            log(LOG_LEVELS["INFO"], f"browsering {URL}")
            self.browser.get(URL)

            log(LOG_LEVELS["INFO"], "parsing content")
            sleep(1)
            content = BeautifulSoup(self.browser.page_source, "html.parser")
            self.browser.close()

            log(LOG_LEVELS["INFO"], "getting movies information")
            return [self._get_movie_content_from_row(row) for row in content.find_all("tr")[1:]]

        except Exception as e:
            log(LOG_LEVELS["ERROR"], f"Unexpected exception occurred: {e.msg}")

    def _get_movie_content_from_row(self, row):
        return {
            "poster_url": self._get_poster_url(row),
            "title": self._get_movie_title(row),
            "imdb_rating": self._get_movie_imdb_ratting(row),
            "movie_details_url": self._get_movie_details_url(row),
        }

    @staticmethod
    def _get_poster_url(row):
        return row.select_one("img").get("src")

    @staticmethod
    def _get_movie_imdb_ratting(row):
        return row.select_one("td.imdbRating").text.replace("\n", "")

    @staticmethod
    def _get_movie_details_url(row):
        return row.select_one("td.titleColumn>a").get("href")

    @staticmethod
    def _get_movie_title(row):
        return row.select_one("td.titleColumn").select_one("a").text

    def _get_full_size_image_poster(self, url):
        MOVIE_DETAILS_POSTER_CLASS = "ipc-lockup-overlay ipc-focusable"
        self.browser.get(url)
        content = BeautifulSoup(self.browser.page_source, "html.parser")
        content.find_element_by_class(MOVIE_DETAILS_POSTER_CLASS)[0]

    def _set_options(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options


if __name__ == "__main__":
    start_time = time()
    ws = WebScrapper()
    movies = ws.scrap_url()
    end_time = time()
    print(movies)
    print(f"It took {round(end_time - start_time, 3)} seconds to run")
