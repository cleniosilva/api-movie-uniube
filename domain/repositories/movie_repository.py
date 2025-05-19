from abc import ABC, abstractmethod
from typing import List
from domain.entities.movie import Movie

class MovieRepository(ABC):
    @abstractmethod
    def create(self, movie: Movie) -> Movie:
        pass

    @abstractmethod
    def get_by_id(self, movie_id: int) -> Movie | None:
        pass

    @abstractmethod
    def get_all(self) -> List[Movie]:
        pass

    @abstractmethod
    def update(self, movie_id: int, movie: Movie) -> Movie | None:
        pass

    @abstractmethod
    def delete(self, movie_id: int) -> bool:
        pass