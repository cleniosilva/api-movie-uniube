from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class UpdateMovie:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, movie_id: int, title: str, year: int, genre: str) -> Movie | None:
        movie = Movie(id=movie_id, title=title, year=year, genre=genre)
        return self.repository.updated(movie_id, movie)