from domain.repositories.movie_repository import MovieRepository

class DeleteMovie:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, movie_id: int) -> bool:
        return self.repository.delete(movie_id)