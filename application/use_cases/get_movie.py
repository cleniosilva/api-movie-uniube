from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class GetMovie:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, movie_id: int) -> Movie | None:
        return self.repository.get_by_id(movie_id)