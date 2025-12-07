from typing import List, Any

import requests
from dotenv import load_dotenv
from tkinter import *
from tkinter import ttk
import os
from sqlmodel import Field, SQLModel, create_engine, Session, select
from datetime import datetime


class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    movie_name: str
    movie_date: datetime
    finished: bool


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

load_dotenv()
API_KEY = os.getenv("API_KEY")


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


def create_movie(new_movie, finished):
    date_lists = new_movie["release_date"].split("-")

    movie = Movie(movie_name=new_movie["original_title"], movie_date=datetime(
        int(date_lists[0]),
        int(date_lists[1]),
        int(date_lists[2])), finished=finished)
    session = Session(engine)
    session.add(movie)
    session.commit()


def get_movie_by_title(title:str):
    session = Session(engine)
    movie = session.exec(select(Movie).where("movie_name" == title)).first()
    if not movie:
        raise FileNotFoundError
    return movie


def get_all_movies():
    session = Session(engine)
    movie_list = session.exec(select(Movie)).all()
    if len(movie_list) == 0:
        raise FileNotFoundError
    return movie_list



def main():
    create_db_and_tables()
    root = Tk()

    movie_name = StringVar()
    movies_items: list[Movie] = []
    movie_choice_list: list[Any] = []
    # noinspection PyTypeChecker
    choice_list_var = StringVar(value=movie_choice_list)

    def on_change_selected_movie(selection):
        print(movies_items[selection[0]])

    def search_movie():
        movies = get_movie(movie_name.get())
        movies_items.extend(movies)
        for item in movies_items:
            print(item)
            mod_item = item["original_title"]
            if item["release_date"]:
                mod_item = mod_item + " - " + item["release_date"]
            movie_choice_list.append(mod_item)
        # noinspection PyTypeChecker
        choice_list_var.set(movie_choice_list)

    frame = ttk.Frame(root, padding=(10,10,10,10))
    frame.grid(column=0, row=0, sticky="NSEW")
    entry_frame = ttk.Frame(frame, padding=(10,10,10,10))
    entry_frame.grid(column=0, row=0)
    entry_label = ttk.Label(entry_frame, text="Enter Movie for Database")
    entry_label.grid(column=0, row=0)
    entry_entry = ttk.Entry(entry_frame, textvariable=movie_name)
    entry_entry.grid(column=1, row=0)
    entry_button = ttk.Button(entry_frame, text="Search", command=search_movie)
    entry_button.grid(column=3, row=0)

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.columnconfigure(0, weight=1)

    list_frame = ttk.Frame(frame, padding=(10,10,10,10))
    list_frame.grid(row=1, column=0, sticky="NSEW")

    list_label = ttk.Label(list_frame, text="Movies")
    list_label.grid(column=0, row=0)

    box = Listbox(list_frame, listvariable=choice_list_var, selectmode="browse")
    box.grid(column=0, row=1, sticky="NSEW")

    list_frame.columnconfigure(0, weight=1)
    list_frame.rowconfigure(1, weight=1)

    box.bind("<Double-1>", lambda e: on_change_selected_movie(box.curselection()))

    root.mainloop()


if __name__ == "__main__":
    main()
