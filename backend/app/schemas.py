from pydantic import BaseModel

class SongSchema(BaseModel):
    name: str
    artist: str
    album: str
    genre: str
    year_released: int
    rating: float

