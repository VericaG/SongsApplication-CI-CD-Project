from motor.motor_asyncio import AsyncIOMotorClient
import os

host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", "27017"))
user = os.getenv("MONGO_USER", "user")
password = os.getenv("MONGO_PASS", "pass")
db_name = os.getenv("MONGO_DB", "testdb")

uri = f"mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin"

client = AsyncIOMotorClient(uri)
db = client[db_name]
song_collection = db["songs"]

