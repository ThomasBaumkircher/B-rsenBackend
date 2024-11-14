from crud.attendee import attendee_crud
from api.api import GenericRouter
from api.model import AttendeeSchema, AttendeeDB, ContactDB, BookingDB


class AttendeeRouter(GenericRouter[AttendeeSchema, AttendeeDB]):
    def __init__(self):
        super().__init__(attendee_crud, AttendeeSchema, AttendeeDB)

        self.add_api_route("/{attendee_id:int}/contact", self.get_contact, methods=["GET"], status_code=200, response_model=ContactDB)
        self.add_api_route("/{attendee_id:int}/bookings", self.get_bookings, methods=["GET"], status_code=200, response_model=list[BookingDB])

    def get_contact(self, attendee_id: int):
        return attendee_crud.get_contact(attendee_id)

    def get_bookings(self, attendee_id: int):
        return attendee_crud.get_bookings(attendee_id)


attendee_router = AttendeeRouter()
