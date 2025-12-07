from tkinter import ttk
from tkinter import *
from functions import get_movie
from Models.Movie import Movie
from constants import DEFAULT_PADDING


class SearchFrame:
    def __init__(self, root):

        movie_name = StringVar()
        movies_items: list[Movie] = []
        movie_choice_list = []
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

        outer_frame = ttk.Frame(root)
        outer_frame.grid(column=0, row=0, padx=10, pady=5, sticky="NSEW")
        outer_frame.columnconfigure(0, weight=1)
        outer_frame.rowconfigure(0, weight=1)

        top_frame = ttk.Frame(outer_frame, padding=DEFAULT_PADDING)
        top_frame.grid(column=0, row=0, sticky="NSEW")
        top_frame['borderwidth'] = 4
        top_frame['relief'] = "groove"

        entry_frame = ttk.Frame(top_frame, padding=DEFAULT_PADDING)
        entry_frame.grid(column=0, row=0, sticky="E")

        entry_label = ttk.Label(entry_frame, text="Enter Movie for Database: ")
        entry_label.grid(column=0, row=0)

        entry_entry = ttk.Entry(entry_frame, textvariable=movie_name)
        entry_entry.grid(column=1, row=0, padx=5)

        entry_button = ttk.Button(entry_frame, text="Search", command=search_movie)
        entry_button.grid(column=3, row=0)

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=1)
        top_frame.rowconfigure(1, weight=4)
        top_frame.rowconfigure(0, weight=1)
        top_frame.columnconfigure(0, weight=1)

        list_frame = ttk.Frame(top_frame, padding=DEFAULT_PADDING)
        list_frame.grid(row=1, column=0, sticky="NSEW")

        list_label = ttk.Label(list_frame, text="Movies")
        list_label.grid(column=0, row=0)

        box = Listbox(list_frame, listvariable=choice_list_var, selectmode="browse")
        box.grid(column=0, row=1, sticky="NSEW")

        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(1, weight=1)

        box.bind("<Double-1>", lambda e: on_change_selected_movie(box.curselection()))