from .db import song_collection
from .schemas import SongSchema

from bson import ObjectId

def fix_id(song):
    if song and "_id" in song:
        song["_id"] = str(song["_id"])
    return song


async def create(song_data: SongSchema):
    existing = await song_collection.find_one({"name": song_data.name})
    if existing:
        return None
    song_dict = song_data.dict()
    await song_collection.insert_one(song_dict)
    return song_dict

async def create(song_data: SongSchema):
    existing = await song_collection.find_one({"name": song_data.name})
    if existing:
        return None
    song_dict = song_data.dict()
    result = await song_collection.insert_one(song_dict)
    song_dict["_id"] = str(result.inserted_id)  # додај го _id како стринг
    return song_dict

async def read(name: str):
    song = await song_collection.find_one({"name": name})
    return fix_id(song)

async def update(song_data: SongSchema):
    result = await song_collection.update_one(
        {"name": song_data.name},
        {"$set": song_data.dict()}
    )
    if result.matched_count == 0:
        return None
    song = await read(song_data.name)
    return song

async def delete(name: str):
    result = await song_collection.delete_one({"name": name})
    if result.deleted_count == 0:
        return None
    return {"message": "Deleted"}

async def list_all():
    songs = []
    cursor = song_collection.find({})
    async for song in cursor:
        songs.append(fix_id(song))
    return songs

