# Real-Time Event Booking API

A high-performance monolithic REST API built with **Python**, **FastAPI**, and **MongoDB** designed for managing event schedules and ticket inventory. The application enforces asynchronous data processing pipelines and maintains strict consistency for concurrent seat allocations.

## 🚀 Key Features

- **Asynchronous Architecture:** Utilizing FastAPI's native ASGI engine alongside the `Motor` async driver to handle I/O-bound database operations concurrently without blocking incoming requests.
- **Schema Enforcement & Validation:** Implements Pydantic schemas for data parsing, automated request payload sanitation, and structural type-hinting.
- **Race Condition Prevention:** Leverages MongoDB's atomic `$inc` operators to process ticket transactions safely at scale, preventing over-allocation anomalies.
- **Self-Documenting API:** Built-in interactive Swagger UI documentation out of the box.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** FastAPI
- **Database:** MongoDB (Local instance)
- **ASGI Server:** Uvicorn
- **Data Validation:** Pydantic v2
- **Database Driver:** Motor (Async MongoDB Driver)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd real-time-event-booking-api
   ```
