from .crud import GenericCRUD
from db.model import Attendee, Contact, Booking
from sqlalchemy import select
from db.session import session


class AttendeeCRUD(GenericCRUD[Attendee]):
    def __init__(self):
        super().__init__(Attendee)

    async def get_contact(self, id: int):
        attendee = await self.get(id)

        stmt = select(Contact).where(Contact.id == attendee.contact_id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj

    async def get_bookings(self, id: int):
        attendee = await self.get(id)

        stmt = select(Booking).where(Booking.attendee_id == attendee.id)
        res = session.execute(stmt)
        obj = res.scalars().all()

        return obj


attendee_crud = AttendeeCRUD()
