from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()  # load .env file

MONGODB_URI = os.getenv("Mongo_Url", "mongodb://localhost:27017")
DB_NAME = os.getenv("db", "employee_db")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

