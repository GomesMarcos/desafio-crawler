def query_save_movie(movie: dict):
    return f"""
        INSERT OR IGNORE INTO movies (
            title,
            ranking,
            year,
            duration,
            age_rating,
            poster_url,
            imdb_rating,
            movie_details_url
        ) values ({_get_movie_query(movie)})
    """


def _get_movie_query(movie):
    return f"""
        "{movie["title"]}",
        {movie["ranking"]},
        {movie["year"]},
        "{movie["duration"]}",
        "{movie["age_rating"]}",
        "{movie["poster_url"]}",
        {movie["imdb_rating"]},
        "{movie["movie_details_url"]}"
    """


def query_create_table_movie():
    return """CREATE TABLE IF NOT EXISTS movie (
        id                  INTEGER PRIMARY KEY,
        title               VARCHAR,
        ranking             INTEGER,
        year                INTEGER,
        duration            VARCHAR,
        age_rating          VARCHAR,
        poster_url          VARCHAR UNIQUE,
        imdb_rating         FLOAT,
        movie_details_url   VARCHAR UNIQUE
    );"""
