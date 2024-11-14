import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


# Inconsistency test

booking = {
    "event_id": 4,
    "attendee_id": 3
}

def add_booking(booking):
    return requests.post("http://localhost:8000/bookings/", json=booking).json()

futures = []
with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(10):
            future = executor.submit(add_booking, booking)
            futures.append(future)

        for future in as_completed(futures):
            result = future.result()
            print(result)
