from tkinter import *
from tkinter import ttk
import os
from sqlmodel import SQLModel, create_engine
from Components.Search import SearchFrame


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_tables()
    root = Tk()
    root.title("Obsidian Movie Maker")
    root.minsize(400, 400)

    SearchFrame(root)

    root.mainloop()


if __name__ == "__main__":
    main()
