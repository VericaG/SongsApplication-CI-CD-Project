from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/songs")
def read_songs(db: Session = Depends(get_db)):
    return crud.get_songs(db)

@app.post("/songs")
def create_song(song: models.SongCreate, db: Session = Depends(get_db)):
    return crud.create_song(db, song)
