from datetime import datetime
from typing import List
from sqlalchemy import Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from db.session import engine

Base = declarative_base()


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    seatnr: Mapped[int] = mapped_column(Integer)
    date: Mapped[datetime] = mapped_column(DateTime)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"))
    attendee_id: Mapped[int] = mapped_column(Integer, ForeignKey("attendees.id"))

    event: Mapped["Event"] = relationship(back_populates="bookings")
    attendee: Mapped["Attendee"] = relationship(back_populates="bookings")


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey("locations.id"))

    location: Mapped["Location"] = relationship(back_populates="events")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="event")
    managers: Mapped[List["Manager"]] = relationship(back_populates="event")


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    events: Mapped[List[Event]] = relationship(back_populates="location")


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)

    attendees: Mapped[List["Attendee"]] = relationship(back_populates="contact")
    managers: Mapped[List["Manager"]] = relationship(back_populates="contact")


class Attendee(Base):
    __tablename__ = "attendees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contact_id: Mapped[int] = mapped_column(Integer, ForeignKey("contacts.id"))

    contact: Mapped["Contact"] = relationship(back_populates="attendees")
    bookings: Mapped[List["Booking"]] = relationship(back_populates="attendee")


class Manager(Base):
    __tablename__ = "managers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contact_id: Mapped[int] = mapped_column(Integer, ForeignKey("contacts.id"))
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"))

    contact: Mapped["Contact"] = relationship(back_populates="managers")
    event: Mapped["Event"] = relationship(back_populates="managers")


Base.metadata.create_all(engine)
