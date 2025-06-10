# import os
#
# from sqlalchemy import create_engine, URL
# from sqlalchemy.orm import sessionmaker
#
# POSTGRES_URL = os.getenv("POSTGRES_URL")
# POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
# POSTGRES_USER = os.getenv("POSTGRES_USER")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
#
# if POSTGRES_URL is None:
#     raise RuntimeError("Environment variable POSTGRES_URL is not set")
#
# if POSTGRES_DATABASE is None:
#     raise RuntimeError("Environment variable POSTGRES_DATABASE is not set")
#
# if POSTGRES_USER is None:
#     raise RuntimeError("Environment variable POSTGRES_USER is not set")
#
# url = URL.create(
#     drivername="postgresql",
#     username=POSTGRES_USER,
#     password=POSTGRES_PASSWORD,
#     host=POSTGRES_URL,
#     database=POSTGRES_DATABASE,
#     port=5432
# )
# engine = create_engine(url)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

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

