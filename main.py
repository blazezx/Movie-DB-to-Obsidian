from tkinter import *
from tkinter import ttk
import os
from sqlmodel import SQLModel, create_engine
from Components.Search import SearchFrame
from Components.display_movie_details import MovieDetails


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    root = Tk()
    root.title("Obsidian Movie Maker")
    root.minsize(500, 500)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)

    SearchFrame(root)
    MovieDetails(root)

    root.mainloop()


if __name__ == "__main__":
    main()
