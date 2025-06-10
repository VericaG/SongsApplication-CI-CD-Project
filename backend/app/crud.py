# from sqlalchemy.orm import Session
# from . import models
# from . import schemas
#
#
# def create(db: Session, schema: schemas.SongSchema):
#     """
#     Create a book.
#
#     Args:
#         db (Session): The database session object.
#         schema (BookSchema): The book schema.
#
#     Returns:
#         Book | None: The created book, unless one with the same ISBN already exists.
#     """
#
#     existing_song = read(db, schema.name)
#
#     if existing_song is not None:
#         return None
#
#     song = models.Song(
#         name=schema.name,
#         artist=schema.artist,
#         genre=schema.genre,
#         year_released=schema.year_released,
#         album=schema.album,
#         rating=schema.rating,
#     )
#     db.add(song)
#     db.commit()
#     db.refresh(song)
#
#     return song
#
#
# def read(db: Session, name: str):
#     """
#     Read a book.
#
#     Args:
#         db (Session): The database session object.
#         isbn (str): The ISBN of the book.
#
#     Returns:
#         Book | None: The book, if it exists.
#     """
#
#     return db.query(models.Song).filter(models.Song.name == name).first()
#
#
# def update(db: Session, schema: schemas.SongSchema):
#     song = read(db, schema.name)
#     if song is None:
#         return None
#
#     song.artist = schema.artist
#     song.genre = schema.genre
#     song.year_released = schema.year_released
#     song.album = schema.album
#     song.rating = schema.rating
#
#     db.commit()
#     db.refresh(song)
#
#     return song
#
#
#
# def delete(db: Session, name: str):
#     """
#     Delete a book.
#
#     Args:
#         db (Session): The database session object.
#         isbn (str): The ISBN of the book.
#
#     Returns:
#         Book | None: The book, if it exists.
#     """
#
#     song = read(db, name)
#
#     if song is None:
#         return None
#
#     db.delete(song)
#     db.commit()
#
#     return song
#
#
# def list_all(db: Session):
#     """
#     Get all books.
#
#     Args:
#         db (Session): The database session object.
#
#     Returns:
#         list[Book]: The list of all books.
#     """
#
#     return db.query(models.Song).all()

from app.db import song_collection
from app.schemas import SongSchema
from bson.objectid import ObjectId

async def create(song_data: SongSchema):
    existing = await song_collection.find_one({"name": song_data.name})
    if existing:
        return None
    song_dict = song_data.dict()
    result = await song_collection.insert_one(song_dict)
    return song_dict

async def read(name: str):
    song = await song_collection.find_one({"name": name})
    return song

async def update(song_data: SongSchema):
    result = await song_collection.update_one(
        {"name": song_data.name}, {"$set": song_data.dict()}
    )
    if result.matched_count == 0:
        return None
    return await read(song_data.name)

async def delete(name: str):
    result = await song_collection.delete_one({"name": name})
    if result.deleted_count == 0:
        return None
    return {"message": "Deleted"}

async def list_all():
    songs = []
    cursor = song_collection.find({})
    async for song in cursor:
        songs.append(song)
    return songs
