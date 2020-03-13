import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    event = Column(String)
