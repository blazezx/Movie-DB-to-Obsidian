import requests
from dotenv import load_dotenv
from tkinter import *
from tkinter import ttk

API_KEY = load_dotenv("API_KEY")


def get_movie(movie):
    movie = movie.replace(" ", "%20")
    url = "https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=false&language=en-US&page=1".format(movie=movie)
    url.encode("utf8")
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer {key}".format(key=API_KEY)
    }

    print(url)

    response = requests.get(url, headers=headers)

    return response.json()


root = Tk()
frame = ttk.Frame(root, padding=(10,10,10,10))
frame.grid(column=0, row=0)





