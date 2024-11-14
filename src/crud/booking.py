from datetime import datetime
from .crud import GenericCRUD
from db.model import Booking, Event, Attendee
from sqlalchemy import select
from db.session import session
from .event import event_crud
from fastapi import HTTPException


class BookingCRUD(GenericCRUD[Booking]):
    def __init__(self):
        super().__init__(Booking)

    async def post(self, payload) -> int:
        try:
            obj = self.model(**vars(payload))
            # Check if there are free seats
            free_seats = await event_crud.get_free_seats(obj.event_id)
            if free_seats <= 0:
                raise HTTPException(status_code=400, detail="No free seats available")
            seatnr = 1
            session.add(obj)
            session.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        return obj.id # type: ignore

    async def get_event(self, id: int):
        booking = await self.get(id)

        stmt = select(Event).where(Event.id == booking.event_id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj

    async def get_attendee(self, id: int):
        booking = await self.get(id)

        stmt = select(Attendee).where(Attendee.id == booking.attendee_id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj


booking_crud = BookingCRUD()
