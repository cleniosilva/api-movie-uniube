from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class MovieUsecase:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def create(self, title: str, year: int, genre: str) -> Movie:
        movie = Movie(id=None, title=title, year=year, genre=genre)
        return self.repository.create(movie)

    def get(self, movie_id: int) -> Movie | None:
        return self.repository.get_by_id(movie_id)

    def delete(self, movie_id: int) -> bool:
        return self.repository.delete(movie_id)

     def listMovie(self) -> List[Movie]:
        return self.repository.get_all()

    def updated(self, movie_id: int, title: str, year: int, genre: str) -> Movie | None:
        movie = Movie(id=movie_id, title=title, year=year, genre=genre)
        return self.repository.updated(movie_id, movie)