from pydantic import BaseModel

class MovieModel(BaseModel):
    id: int | None = None
    title: str
    year: int
    genre: str