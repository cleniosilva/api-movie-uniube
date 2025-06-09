from fastapi import FastAPI, HTTPException
from typing import List
from application.use_cases.movie_usecase import MovieUsecase
from infrastructure.database.sqlite_repository import SQLiteMovieRepository
from presentation.fastapi.models import MovieModel

app = FastAPI()

repository = SQLiteMovieRepository("movies.db")
movie_usecase = MovieUsecase()


@app.post("/movies/", response_model=MovieModel)
def create_movie(movie: MovieModel):
    created_movie = movie_usecase.create(movie.title, movie.year, movie.genre)
    return MovieModel(id=created_movie.id, title=created_movie.title, year=created_movie.year, genre=created_movie.genre)

@app.get("/movies/", response_model=List[MovieModel])
def get_movies():
    movies = movie_usecase.listMovie()
    return [MovieModel(id=m.id, title=m.title, year=m.year, genre=m.genre) for m in movies]

@app.get("/movies/{movie_id}", response_model=MovieModel)
def get_movie(movie_id: int):
    movie = movie_usecase.get(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieModel(id=movie.id, title=movie.title, year=movie.year, genre=movie.genre)

@app.put("/movies/{movie_id}", response_model=MovieModel)
def update_movie(movie_id: int, movie: MovieModel):
    updated_movie = movie_usecase.updated(movie_id, movie.title, movie.year, movie.genre)
    if updated_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieModel(id=updated_movie.id, title=updated_movie.title, year=updated_movie.year, genre=updated_movie.genre)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    success = movie_usecase.delete(movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"detail": "Movie deleted"}