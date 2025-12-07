from sqlmodel import SQLModel, Field
from datetime import datetime


class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    movie_name: str
    movie_date: datetime
    finished: bool
