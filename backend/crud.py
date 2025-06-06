from sqlalchemy.orm import Session
from models import Song, SongCreate

def get_songs(db: Session):
    return db.query(Song).all()

def create_song(db: Session, song: SongCreate):
    db_song = Song(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song
