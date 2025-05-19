from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class CreateMovie:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, title: str, year: int, genre: str) -> Movie:
        movie = Movie(id=None, title=title, year=year, genre=genre)
        return self.repository.create(movie)