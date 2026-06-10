from pydantic import BaseModel, Field
from typing import Optional

# This schema defines what data we EXPECT when creating a new event (Request Body)
class EventCreateSchema(BaseModel):
    title: str = Field(..., example="Tech Conference 2026")
    description: str = Field(..., example="Annual gathering of software engineers.")
    location: str = Field(..., example="Colombo, Sri Lanka")
    total_tickets: int = Field(..., gt=0, example=100)  # gt=0 means greater than 0
    available_tickets: int = Field(..., gt=-1, example=100)

# This schema defines what data we RETURN to the user (Response Body)
# MongoDB uses ObjectIDs (_id), so we need to convert them to strings for the frontend
class EventResponseSchema(BaseModel):
    id: str
    title: str
    description: str
    location: str
    total_tickets: int
    available_tickets: int

    class Config:
        # This tells Pydantic to parse arbitrary object attributes (like MongoDB dict keys)
        from_attributes = True