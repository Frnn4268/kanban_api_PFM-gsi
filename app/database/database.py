import os
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

# The database connection URL for MongoDB, fetched from the environment variable 'MONGO_URL'
# or set to a default value if the environment variable is not found.
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# MongoDB client using Motor's AsyncIOMotorClient to interact with MongoDB asynchronously.
# This client is responsible for handling the connection to the MongoDB server.
client = AsyncIOMotorClient(MONGO_URL)

# AIOEngine is the ODMantic engine used to interact with the MongoDB database.
# It is an asynchronous engine that allows performing CRUD operations on the database.
# The engine is configured to work with the 'kanban_db' database by default.
engine = AIOEngine(client=client, database="kanban_db")
