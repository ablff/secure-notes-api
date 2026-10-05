# Secure Notes API

A secure backend API built for portfolio evaluation, featuring data validation, ORM mapping, and robust database integration.

## Tech Stack

- Python (Programming Language)
- FastAPI (Web Framework & ASGI)
- SQLAlchemy (Object-Relational Mapper)
- PostgreSQL (Relational Database)
- Docker (Containerization)
- Pydantic (Data Validation)

## Architecture & Features

- Database Integration: Managed via PostgreSQL running inside a Docker container with strict network mapping.
- ORM Layer: Uses SQLAlchemy models to map Python classes to relational tables securely, preventing SQL injection vulnerabilities.
- Data Validation: Request payload validation handled via Pydantic schemas separating API contracts from database models.
- Dependency Injection: Robust database session lifecycle management ensuring connection cleanup and thread safety.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker

### Environment Setup

1. Clone the repository:
   git clone [https://github.com/ablff/secure-notes-api.git](https://github.com/ablff/secure-notes-api.git)
   cd secure-notes-api

2. Start the PostgreSQL database using Docker:
    docker run --name secure-notes-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=adminpass -e POSTGRES_DB=notes_db -p 5432:5432 -d postgres:15-alpine

3. Install dependencies:
    pip install -r requirements.txt

4. Run the development server:
    uvicorn main:app --reload

API documentation and interective Swagger UI will be available at /docs