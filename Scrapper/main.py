from logging import getLevelNamesMapping, log
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window_size=400,800")

URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
LOG_LEVELS = getLevelNamesMapping()

try:
    log(LOG_LEVELS["INFO"], f"browsering {URL}")
    browser = webdriver.Firefox()
    browser.get(URL)
    # sleep(1)

    log(LOG_LEVELS["INFO"], "generating content")
    content = BeautifulSoup(browser.page_source, "html.parser")
    movies = [get_movie_content_from_row(row) for row in content.find_all('tr')[1:]]
    browser.close()

except Exception as e:
    log(LOG_LEVELS["ERROR"], f"Unexpected exception occurred: {e.args[0]}")

print(content.prettify())


def get_movie_content_from_row(row):
    # TODO: finish poster and rating fields
    return {
        "poster": ...,
        "title": row.select('td.titleColumn')[0].select('a')[0].text,
        "imdb_rating": ...,
    }
