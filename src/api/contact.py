from crud.contact import contact_crud
from api.api import GenericRouter
from api.model import ContactSchema, ContactDB


class ContactRouter(GenericRouter[ContactSchema, ContactDB]):
    def __init__(self):
        super().__init__(contact_crud, ContactSchema, ContactDB)


contact_router = ContactRouter()
