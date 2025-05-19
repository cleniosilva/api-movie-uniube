from typing import List
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class ListMovies:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self) -> List[Movie]:
        return self.repository.get_all()