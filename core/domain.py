from typing import NamedTuple

class Book(NamedTuple):
    id: str
    title: str
    author: str
    genre: str
    tags: tuple[str, ...]
    year: int
