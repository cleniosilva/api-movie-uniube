import sqlite3
from typing import List
from domain.entities.movie import Movie
from domain.repositories.movie_repository import MovieRepository

class SQLiteMovieRepository(MovieRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    genre TEXT NOT NULL
                )
            """)
            conn.commit()

    def create(self, movie: Movie) -> Movie:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO movies (title, year, genre) VALUES (?, ?, ?)",
                (movie.title, movie.year, movie.genre)
            )
            movie.id = cursor.lastrowid
            conn.commit()
        return movie

    def get_by_id(self, movie_id: int) -> Movie | None:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, year, genre FROM movies WHERE id = ?", (movie_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return Movie(id=row["id"], title=row["title"], year=row["year"], genre=row["genre"])

    def get_all(self) -> List[Movie]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, year, genre FROM movies")
            rows = cursor.fetchall()
            return [Movie(id=row["id"], title=row["title"], year=row["year"], genre=row["genre"]) for row in rows]

    def update(self, movie_id: int, movie: Movie) -> Movie | None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE movies SET title = ?, year = ?, genre = ? WHERE id = ?",
                (movie.title, movie.year, movie.genre, movie_id)
            )
            if cursor.rowcount == 0:
                return None
            conn.commit()
            movie.id = movie_id
            return movie

    def delete(self, movie_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
            if cursor.rowcount == 0:
                return False
            conn.commit()
            return True