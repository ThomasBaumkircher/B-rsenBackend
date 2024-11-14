from crud.event import event_crud
from api.api import GenericRouter
from api.model import EventSchema, EventDB, LocationDB, BookingDB, ManagerDB


class EventRouter(GenericRouter[EventSchema, EventDB]):
    def __init__(self):
        super().__init__(event_crud, EventSchema, EventDB)

        self.add_api_route("/{event_id:int}/location", self.get_location, methods=["GET"], status_code=200, response_model=LocationDB)
        self.add_api_route("/{event_id:int}/bookings", self.get_bookings, methods=["GET"], status_code=200, response_model=list[BookingDB])
        self.add_api_route("/{event_id:int}/managers", self.get_managers, methods=["GET"], status_code=200, response_model=list[ManagerDB])
        self.add_api_route("/next_month", self.get_next_month, methods=["GET"], status_code=200, response_model=list[EventDB])

    def get_location(self, event_id: int):
        return event_crud.get_location(event_id)

    def get_bookings(self, event_id: int):
        return event_crud.get_bookings(event_id)

    def get_managers(self, event_id: int):
        return event_crud.get_managers(event_id)

    def get_next_month(self):
        return event_crud.get_next_month()

event_router = EventRouter()
