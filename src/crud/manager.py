from .crud import GenericCRUD
from db.model import Manager, Contact, Event
from sqlalchemy import select
from db.session import session


class ManagerCRUD(GenericCRUD[Manager]):
    def __init__(self):
        super().__init__(Manager)

    async def get_contact(self, id: int):
        manager = await self.get(id)

        stmt = select(Contact).where(Contact.id == manager.contact_id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj

    async def get_event(self, id: int):
        manager = await self.get(id)

        stmt = select(Event).where(Event.manager_id == manager.id)
        res = session.execute(stmt)
        obj = res.scalar()

        return obj


manager_crud = ManagerCRUD()
