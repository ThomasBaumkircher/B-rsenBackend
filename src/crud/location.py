from .crud import GenericCRUD
from db.model import Location, Event
from sqlalchemy import select
from db.session import session


class LocationCRUD(GenericCRUD[Location]):
    def __init__(self):
        super().__init__(Location)

    async def get_events(self, id: int):
        location = await self.get(id)

        stmt = select(Event).where(Event.location_id == location.id)
        res = session.execute(stmt)
        obj = res.scalars().all()

        return obj


location_crud = LocationCRUD()
