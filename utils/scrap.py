import json
import sys

from selenium.webdriver.common.by import By

sys.path.append(".")
from utils import JSON_FILENAME, SCREENSHOT_FILENAME, log_message


def get_all_movies(driver):
    movies = driver.find_element(By.CLASS_NAME, "ipc-metadata-list--dividers-between")
    movies.screenshot(SCREENSHOT_FILENAME)
    yield from movies.find_elements(By.TAG_NAME, "li")


def get_poster_url(row):
    return row.find_element(By.TAG_NAME, "img").get_attribute("src")


def get_movie_imdb_ratting(row):
    return row.find_element(By.CLASS_NAME, "ipc-rating-star").text


def get_movie_details_url(row):
    return row.find_element(By.CLASS_NAME, "ipc-title-link-wrapper").get_attribute("href")


def get_movie_title(row):
    return row.find_element(By.TAG_NAME, "h3").text.split(".")[1].strip()


def get_movie_ranking(row):
    return row.find_element(By.TAG_NAME, "h3").text.split(".")[0].strip()


def get_movie_year(row):
    return row.find_elements(By.CLASS_NAME, "cli-title-metadata-item")[0].text


def get_movie_duration(row):
    return row.find_elements(By.CLASS_NAME, "cli-title-metadata-item")[1].text


def get_movie_age_rating(row):
    try:
        return row.find_elements(By.CLASS_NAME, "cli-title-metadata-item")[2].text
    except IndexError:
        return "Not Rated"


def get_movie_info(row):
    return {
        "title": get_movie_title(row),
        "ranking": get_movie_ranking(row),
        "year": get_movie_year(row),
        "duration": get_movie_duration(row),
        "age_rating": get_movie_age_rating(row),
        "poster_url": get_poster_url(row),
        "imdb_rating": get_movie_imdb_ratting(row),
        "movie_details_url": get_movie_details_url(row),
    }


def prepare_ending_json_file(file):
    from os import SEEK_END
    file.close()

    log_message("Handling last json object ending with comma")
    with open(JSON_FILENAME, "+rb") as file:
        file.seek(-3, SEEK_END)
        file.write(b"}\n]")
        log_message("All JSON movies saved successfully")


def save_movie_into_json(movie, is_start=False, is_end=False):
    with open(JSON_FILENAME, "a", encoding="utf-8") as file:
        if is_start:
            file.write("[")
        if not is_start and not is_end:
            json.dump(movie, file)
            file.write(",\n")
        if is_end:
            prepare_ending_json_file(file)
