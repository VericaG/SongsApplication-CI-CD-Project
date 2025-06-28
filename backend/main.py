from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import SongSchema
from app.crud import create, read, update, delete, list_all

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
