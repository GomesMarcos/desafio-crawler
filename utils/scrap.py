import json
import sys


sys.path.append(".")
from utils import JSON_FILENAME, SCREENSHOT_FILENAME, log_message


def get_all_movies(driver):
    movies = driver.find_element("class name", "ipc-metadata-list--dividers-between")
    movies.screenshot(SCREENSHOT_FILENAME)
    yield from movies.find_elements("tag name", "li")


def get_poster_url(row):
    return row.find_element("tag name", "img").get_attribute("src")


def get_movie_imdb_ratting(row):
    return row.find_element("class name", "ipc-rating-star").text


def get_movie_details_url(row):
    return row.find_element("class name", "ipc-title-link-wrapper").get_attribute("href")


def get_movie_title(row):
    return row.find_element("tag name", "h3").text.split(".")[1].strip()


def get_movie_position(row):
    return row.find_element("tag name", "h3").text.split(".")[0].strip()


def get_movie_year(row):
    return row.find_elements("class name", "cli-title-metadata-item")[0].text


def get_movie_duration(row):
    return row.find_elements("class name", "cli-title-metadata-item")[1].text


def get_movie_age_rating(row):
    try:
        return row.find_elements("class name", "cli-title-metadata-item")[2].text
    except IndexError:
        return "Not Rated"


def get_movie_info(row):
    return {
        "title": get_movie_title(row),
        "position": get_movie_position(row),
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

    with open(file.name, "+rb") as file:
        file.seek(-3, SEEK_END)
        file.write(b"}\n]")


def save_movies_into_json(movies):
    with open(JSON_FILENAME, "w+", encoding="utf-8") as file:
        try:
            log_message("saving movies information")
            file.write("[")
            while movies:
                movie = get_movie_info(next(movies))
                json.dump(movie, file)
                file.write(",\n")
        except StopIteration:
            log_message("Handling last json object ending with comma")
            prepare_ending_json_file(file)
            log_message("All JSON movies saved successfully")


def save_movies_into_db(movies):
    log_message("Start saving movies into DB")
    ...
