from tkinter import ttk
from tkinter import *
from constants import DEFAULT_PADDING


class MovieDetails:
    def __init__(self, root):

        outer_frame = ttk.Frame(root, padding=DEFAULT_PADDING, width=10, height=12)
        outer_frame.grid(row=1, column=0, sticky="NSEW", padx=10, pady=5)
        outer_frame['borderwidth'] = 4
        outer_frame['relief'] = "groove"

        outer_frame.columnconfigure(0, weight=1)
        outer_frame.rowconfigure(0, weight=1)

        ttk.Label(outer_frame, text="Movie Details").grid()
