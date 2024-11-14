from starlette.exceptions import HTTPException
from .crud import GenericCRUD
from db.model import Event, Location, Booking, Manager
from sqlalchemy import select
from db.session import session
from datetime import date


class EventCRUD(GenericCRUD[Event]):
    def __init__(self):
        super().__init__(Event)

    async def get_location(self, id: int):
        event = await self.get(id)

        stmt = select(Location).where(Location.id == event.location_id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj

    async def get_bookings(self, id: int):
        event = await self.get(id)

        stmt = select(Booking).where(Booking.event_id == event.id)
        res = session.execute(stmt)
        objs = res.scalars().all()

        return objs

    async def get_managers(self, id: int):
        event = await self.get(id)

        stmt = select(Manager).where(Manager.event_id == event.id)
        res = session.execute(stmt)
        objs = res.scalars().all()

        return objs

    async def get_next_month(self):
        stmt = select(Event).where((Event.date >= date.today()) & (Event.date <= date.today().replace(month=date.today().month + 1)))
        res = session.execute(stmt)
        objs = res.scalars().all()

        return objs

    async def get_free_seats(self, id: int):
        event = await self.get(id)

        stmt = select(Booking).where(Booking.event_id == id)
        res = session.execute(stmt)
        bookings = res.scalars().all()

        stmt = select(Location).where(Location.id == event.location_id)
        res = session.execute(stmt)
        location = res.scalar()

        return location.capacity - len(bookings)


event_crud = EventCRUD()
