from fastapi import FastAPI
from app.routers import router as EventRouter


app = FastAPI(
    title="Event Booking API",
    description="A simple API for managing event bookings using FastAPI and MongoDB.",
    version="1.0.0"
)

app.include_router(EventRouter)

@app.get("/")
def read_root():
    return {"message": "Hello, World! (FastAPI)"}