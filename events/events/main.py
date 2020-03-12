from typing import List

from fastapi import Depends, FastAPI

from sqlalchemy.orm import Session

from .database import SessionLocal

from . import crud, schemas

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/events/", response_model=List[schemas.Event])
async def list(db: Session = Depends(get_db)):
    events = crud.get_events(db)
    return events


@app.post("/events/", response_model=schemas.Event)
async def create(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return crud.create_event(db=db, event=event)
