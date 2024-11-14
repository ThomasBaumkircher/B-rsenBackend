from crud.manager import manager_crud
from api.api import GenericRouter
from api.model import ManagerSchema, ManagerDB, ContactDB, EventDB


class ManagerRouter(GenericRouter[ManagerSchema, ManagerDB]):
    def __init__(self):
        super().__init__(manager_crud, ManagerSchema, ManagerDB)

        self.add_api_route("/{manager_id:int}/contact", self.get_contact, methods=["GET"], status_code=200, response_model=ContactDB)
        self.add_api_route("/{manager_id:int}/event", self.get_event, methods=["GET"], status_code=200, response_model=EventDB)

    def get_contact(self, manager_id: int):
        return manager_crud.get_contact(manager_id)

    def get_event(self, manager_id: int):
        return manager_crud.get_event(manager_id)


manager_router = ManagerRouter()
