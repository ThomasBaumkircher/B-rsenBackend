from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.attendee import attendee_router
from api.booking import booking_router
from api.contact import contact_router
from api.event import event_router
from api.location import location_router
from api.manager import manager_router

from db.session import metadata, engine

metadata.create_all(engine)


app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Routers

app.include_router(attendee_router)
app.include_router(booking_router)
app.include_router(contact_router)
app.include_router(event_router)
app.include_router(location_router)
app.include_router(manager_router)
