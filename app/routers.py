from fastapi import APIRouter, HTTPException, status
from app.config import event_collection
from app.models import EventCreateSchema, EventResponseSchema
from typing import List
from bson import ObjectId

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

# Helper function to convert MongoDB BSON document to Python dict mapping our Pydantic schema
def event_helper(event) -> dict:
    return {
        "id": str(event["_id"]),
        "title": event["title"],
        "description": event["description"],
        "location": event["location"],
        "total_tickets": event["total_tickets"],
        "available_tickets": event["available_tickets"]
    }

# --- ENDPOINT 1: CREATE A NEW EVENT (POST) ---
@router.post("/", response_model=EventResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_event(payload: EventCreateSchema):
    # Convert Pydantic object to a standard Python dictionary
    event_dict = payload.model_dump()
    
    # Insert asynchronously into local MongoDB
    new_event = await event_collection.insert_one(event_dict)
    
    # Fetch the newly created document using its generated ObjectId
    created_event = await event_collection.find_one({"_id": new_event.inserted_id})
    
    return event_helper(created_event)

# --- ENDPOINT 2: GET ALL EVENTS (GET) ---
@router.get("/", response_model=List[EventResponseSchema])
async def get_all_events():
    events = []
    # Fetch documents using an async for-loop cursor provided by Motor
    async for event in event_collection.find():
        events.append(event_helper(event))
    return events

@router.post("/{event_id}/book", response_model=EventResponseSchema)
async def book_ticket(event_id: str):
    if not ObjectId.is_valid(event_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid event ID format."
        )
    
    event = await event_collection.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found."
        )
    
    if event["available_tickets"] <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No tickets available for this event."
        )
    
    await event_collection.update_one(
        {"_id": ObjectId(event_id)},
        {"$inc": {"available_tickets": -1}}
    )
    
    updated_event = await event_collection.find_one({"_id": ObjectId(event_id)})
    return event_helper(updated_event)