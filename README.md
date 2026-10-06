# Secure Notes API

A backend API for storing notes, built as a portfolio project to practice REST API design with FastAPI, SQLAlchemy and PostgreSQL.

## Tech Stack

- Python 3.10+
- FastAPI (web framework)
- Uvicorn (ASGI server)
- SQLAlchemy (ORM)
- PostgreSQL (relational database, running in Docker)
- Psycopg2 (PostgreSQL driver)
- Pydantic (data validation)
- python-dotenv (environment variable loading)

## Features

- **Database integration:** PostgreSQL running in a Docker container.
- **ORM layer:** SQLAlchemy models with parameterized queries, which mitigates SQL injection.
- **Data validation:** Pydantic schemas separate the API contract from the database models.
- **Session management:** a `get_db` dependency opens one database session per request and always closes it.
- **Configuration:** credentials are loaded from environment variables and are never stored in the code.

## Getting Started

### Prerequisites

- Python 3.10+
- Docker

### Setup

1. Clone the repository:

```
   git clone https://github.com/ablff/secure-notes-api.git
   cd secure-notes-api
```

2. Create your environment file from the example:

```
   cp .env.example .env
```

   Then edit `.env` and replace the placeholder password with your own.

3. Start the PostgreSQL container. The password must match the one in your `.env`:

```
   docker run --name secure-notes-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=your_password_here -e POSTGRES_DB=notes_db -p 5432:5432 -d postgres:15-alpine
```

4. Install the dependencies:

```
   pip install -r requirements.txt
```

5. Run the development server:

```
   uvicorn main:app --reload
```

The interactive Swagger UI will be available at `/docs`.

## Current Endpoints

| Method | Path       | Description                |
|--------|------------|----------------------------|
| GET    | `/`        | Health check               |
| POST   | `/notes/`  | Create a new note          |

## Roadmap

- [ ] List all notes (`GET /notes/`)
- [ ] Get a note by ID (`GET /notes/{note_id}`)
- [ ] Update a note
- [ ] Delete a note
- [ ] Length validation for note fields
- [ ] Automated tests