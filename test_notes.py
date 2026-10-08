from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest

from main import app, get_db
from database import Base

test_engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_database():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


def test_create_note():
    response = client.post("/notes/", json={"title": "Test", "content": "Hello"})

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test"
    assert data["content"] == "Hello"
    assert "id" in data

def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_note_by_id():
    created = client.post("/notes/", json={"title": "A", "content": "B"})
    note_id = created.json()["id"]

    response = client.get(f"/notes/{note_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "A"


def test_get_note_not_found():

    response = client.get("/notes/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

def test_list_notes_empty():

    response = client.get("/notes/")

    assert response.status_code == 200
    assert response.json() == []

def test_list_notes_one():
    client.post("/notes/", json={"title": "A", "content": "B"})

    response = client.get("/notes/")
    data =response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "A"