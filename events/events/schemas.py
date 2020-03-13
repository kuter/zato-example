import datetime

from pydantic import BaseModel


class EventBase(BaseModel):
    event: str


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True
