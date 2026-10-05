from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models  
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Notes API", version="1.0.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")

def health_check():
    return {"status": "sucess", "message": "Secure Vault is online and connected"}


@app.post("/notes/", response_model=schemas.NoteResponse)

def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    new_note = models.Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note