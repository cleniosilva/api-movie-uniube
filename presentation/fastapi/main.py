from fastapi import FastAPI, HTTPException
from typing import List
from application.use_cases.create_movie import CreateMovie
from application.use_cases.get_movie import GetMovie
from application.use_cases.list_movies import ListMovies
from application.use_cases.update_movie import UpdateMovie
from application.use_cases.delete_movie import DeleteMovie
from infrastructure.database.sqlite_repository import SQLiteMovieRepository
from presentation.fastapi.models import MovieModel

app = FastAPI()

repository = SQLiteMovieRepository("movies.db")
create_movie_use_case = CreateMovie(repository)
get_movie_use_case = GetMovie(repository)
list_movies_use_case = ListMovies(repository)
update_movie_use_case = UpdateMovie(repository)
delete_movie_use_case = DeleteMovie(repository)


@app.post("/movies/", response_model=MovieModel)
def create_movie(movie: MovieModel):
    created_movie = create_movie_use_case.execute(movie.title, movie.year, movie.genre)
    return MovieModel(id=created_movie.id, title=created_movie.title, year=created_movie.year, genre=created_movie.genre)

@app.get("/movies/", response_model=List[MovieModel])
def get_movies():
    movies = list_movies_use_case.execute()
    return [MovieModel(id=m.id, title=m.title, year=m.year, genre=m.genre) for m in movies]

@app.get("/movies/{movie_id}", response_model=MovieModel)
def get_movie(movie_id: int):
    movie = get_movie_use_case.execute(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieModel(id=movie.id, title=movie.title, year=movie.year, genre=movie.genre)

@app.put("/movies/{movie_id}", response_model=MovieModel)
def update_movie(movie_id: int, movie: MovieModel):
    updated_movie = update_movie_use_case.execute(movie_id, movie.title, movie.year, movie.genre)
    if updated_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieModel(id=updated_movie.id, title=updated_movie.title, year=updated_movie.year, genre=updated_movie.genre)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    success = delete_movie_use_case.execute(movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"detail": "Movie deleted"}