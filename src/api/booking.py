from crud.booking import booking_crud
from api.api import GenericRouter
from api.model import BookingSchema, BookingDB, EventDB, AttendeeDB


class BookingRouter(GenericRouter[BookingSchema, BookingDB]):
    def __init__(self):
        super().__init__(booking_crud, BookingSchema, BookingDB)

        self.add_api_route("/{booking_id:int}/event", self.get_event, methods=["GET"], status_code=200, response_model=EventDB)
        self.add_api_route("/{booking_id:int}/attendee", self.get_attendee, methods=["GET"], status_code=200, response_model=AttendeeDB)

    def get_event(self, booking_id: int):
        return booking_crud.get_event(booking_id)

    def get_attendee(self, booking_id: int):
        return booking_crud.get_attendee(booking_id)


booking_router = BookingRouter()
