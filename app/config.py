import motor.motor_asyncio

# If running MongoDB locally, use this URI. Otherwise, paste your Atlas URI string here.
MONGO_DETAILS = "mongodb://localhost:27017"

# Initialize the async client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Create/Access our database (FastAPI will auto-create this if it doesn't exist)
database = client.event_booking_db

# Create/Access our collection
event_collection = database.get_collection("events")