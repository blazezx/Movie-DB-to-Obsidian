import requests
from datetime import datetime
from sqlmodel import Session, select
from Models.Movie import Movie
from constants import API_KEY



def get_movie(movie):
    movie = movie.replace(" ", "%20")
    url = "https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1".format(movie=movie)
    url.encode("utf8")
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {key}".format(key=API_KEY)
    }

    response = requests.get(url, headers=headers)

    return response.json()["results"]


def create_movie(new_movie, finished, engine):
    date_lists = new_movie["release_date"].split("-")

    movie = Movie(movie_name=new_movie["original_title"], movie_date=datetime(
        int(date_lists[0]),
        int(date_lists[1]),
        int(date_lists[2])), finished=finished)
    session = Session(engine)
    session.add(movie)
    session.commit()


def get_movie_by_title(title: str, engine):
    session = Session(engine)
    movie = session.exec(select(Movie).where("movie_name" == title)).first()
    if not movie:
        raise FileNotFoundError
    return movie


def get_all_movies(engine):
    session = Session(engine)
    movie_list = session.exec(select(Movie)).all()
    if len(movie_list) == 0:
        raise FileNotFoundError

    return movie_list
