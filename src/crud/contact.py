from .crud import GenericCRUD
from db.model import Contact, Attendee, Manager
from sqlalchemy import select
from db.session import session


class ContactCRUD(GenericCRUD[Contact]):
    def __init__(self):
        super().__init__(Contact)


contact_crud = ContactCRUD()
