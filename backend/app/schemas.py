from pydantic import BaseModel


class SongSchema(BaseModel):
    name: str
    artist: str
    genre: str
    year_released: int
    album: str
    rating: float