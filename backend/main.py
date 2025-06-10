# import time
#
# from fastapi import Depends, FastAPI
# from sqlalchemy.exc import OperationalError
# from sqlalchemy.orm import Session
#
# from app.crud import create, delete, list_all, read, update
# from app.db import SessionLocal, engine
# from app.models import Base
# from app.schemas import SongSchema
#
#
# from fastapi.middleware.cors import CORSMiddleware
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # или ["http://localhost:8080"]
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
#
# for i in range(5):
#     try:
#         Base.metadata.create_all(bind=engine)
#         break
#     except OperationalError:
#         time.sleep(i + 1)
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello"}
#
#
# @app.post("/create")
# async def create_song(schema: SongSchema, db: Session = Depends(get_db)):
#     song = create(db, schema)
#
#     if song is None:
#         return {"message": "Song already exists"}
#     else:
#         return song
#
#
# @app.get("/read/{name}")
# async def read_song(name: str, db: Session = Depends(get_db)):  # fix: use 'name' not 'song'
#     song = read(db, name)
#     if song is None:
#         return {"message": "Song not found"}
#     return song
#
#
#
# @app.post("/update")
# async def update_song(schema: SongSchema, db: Session = Depends(get_db)):
#     song = update(db, schema)
#
#     if song is None:
#         return {"message": "Song not found"}
#     else:
#         return song
#
#
# @app.post("/delete/{name}")
# async def delete_song(name: str, db: Session = Depends(get_db)):
#     song = delete(db, name)
#
#     if song is None:
#         return {"message": "Song not found"}
#     else:
#         return song
#
#
# @app.get("/list")
# async def list_all_songs(db: Session = Depends(get_db)):
#     return list_all(db)


from fastapi import FastAPI, HTTPException
from app.schemas import SongSchema
from app.crud import create, read, update, delete, list_all

app = FastAPI()

@app.post("/create")
async def create_song(schema: SongSchema):
    song = await create(schema)
    if song is None:
        raise HTTPException(status_code=400, detail="Song already exists")
    return song

@app.get("/read/{name}")
async def read_song(name: str):
    song = await read(name)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.post("/update")
async def update_song(schema: SongSchema):
    song = await update(schema)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.post("/delete/{name}")
async def delete_song(name: str):
    result = await delete(name)
    if result is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return result

@app.get("/list")
async def list_all_songs():
    return await list_all()
