from sqlalchemy.orm import Session

from . import models, schemas


def get_events(db: Session):
    return db.query(models.Event).all()


def create_event(db: Session, event: schemas.Event):
    db_event = models.Event(event=event.event)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
