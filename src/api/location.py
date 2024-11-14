from crud.location import location_crud
from api.api import GenericRouter
from api.model import LocationSchema, LocationDB, EventDB


class LocationRouter(GenericRouter[LocationSchema, LocationDB]):
    def __init__(self):
        super().__init__(location_crud, LocationSchema, LocationDB)

        self.add_api_route("/{location_id:int}/events", self.get_events, methods=["GET"], status_code=200, response_model=list[EventDB])

    def get_events(self, location_id: int):
        return location_crud.get_events(location_id)


location_router = LocationRouter()
