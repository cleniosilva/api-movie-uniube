from dataclasses import dataclass

@dataclass
class Movie:
    id: int | None
    title: str
    year: int
    genre: str