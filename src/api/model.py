from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class BookingSchema(BaseModel):
    event_id: int
    attendee_id: int

class EventSchema(BaseModel):
    name: str
    date: datetime
    location_id: int

class LocationSchema(BaseModel):
    name: str
    capacity: int

class ContactSchema(BaseModel):
    name: str
    email: str
    phone: str

class AttendeeSchema(BaseModel):
    contact_id: int

class ManagerSchema(BaseModel):
    contact_id: int
    event_id: int


class BookingDB(BookingSchema):
    seatnr: int
    date: datetime
    id: int

class EventDB(EventSchema):
    id: int

class LocationDB(LocationSchema):
    id: int

class ContactDB(ContactSchema):
    id: int

class AttendeeDB(AttendeeSchema):
    id: int

class ManagerDB(ManagerSchema):
    id: int
