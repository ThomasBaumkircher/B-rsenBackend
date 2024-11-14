import json
import pytest

from crud.user import user_crud as crud
from api.model import UserDB, WorkhourDB


def test_create_user(test_app, monkeypatch):
    test_request_payload = {
        "username": "test user",
        "is_superuser": False,
    }
    test_response_payload = {
        "id": 1,
        "username": "test user",
        "is_superuser": False,
    }

    async def mock_post(*_):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/users/", json=test_request_payload)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_user_empty_json(test_app):
    response = test_app.post("/users/", json={})
    assert response.status_code == 422


def test_create_user_invalid_json(test_app):
    response = test_app.post("/users/", json={"ame": "test user"})
    assert response.status_code == 422


def test_get_single_user(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "username": "test user",
        "is_superuser": False,
    }

    async def mock_get(*_):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/users/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_single_user_not_found(test_app, monkeypatch):
    async def mock_get(*_):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/users/999/")
    assert response.status_code == 404


def test_get_all_users(test_app, monkeypatch):
    test_data = [
        {
            "id": 1,
            "username": "test user 1",
            "is_superuser": False,
        },
        {
            "id": 2,
            "username": "test user 2",
            "is_superuser": False,
        },
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/users/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_put_user(test_app, monkeypatch):
    test_request_payload = {
        "id": 1,
        "username": "test user",
        "is_superuser": False,
    }
    test_crud_payload = {
        "id": 1,
        "username": "test user",
        "is_superuser": False,
    }
    test_response_payload = {
        "id": 1,
        "username": "test user",
        "is_superuser": False,
    }

    async def mock_put(*_):
        return test_crud_payload

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/users/1/", json=test_request_payload)

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_put_user_not_found(test_app, monkeypatch):
    test_request_payload = {
        "username": "test user",
        "is_superuser": False,
    }

    async def mock_put(*_):
        return None

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/users/999/", json=test_request_payload)

    assert response.status_code == 404


def test_delete_user(test_app, monkeypatch):
    async def mock_delete(*_):
        return 1

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/users/1/")
    assert response.status_code == 200
    assert response.json() == {"detail": "Deleted"}


def test_delete_user_not_found(test_app, monkeypatch):
    async def mock_delete(*_):
        return None

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/users/999/")
    assert response.status_code == 404


def test_get_workhours(test_app, monkeypatch):
    test_data = [
        {
            "id": 1,
            "user_id": 1,
            "project_id": 1,
            "start_date": "2021-01-01T00:00:00",
            "end_date": "2021-01-01T08:00:00",
        },
        {
            "id": 2,
            "user_id": 1,
            "project_id": 1,
            "start_date": "2021-01-01T09:00:00",
            "end_date": "2021-01-01T17:00:00",
        },
    ]

    async def mock_get_workhours(*_):
        return test_data

    monkeypatch.setattr(crud, "get_workhours", mock_get_workhours)

    response = test_app.get("/users/1/workhours/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_workhours_not_found(test_app, monkeypatch):
    async def mock_get_workhours(*_):
        return None

    monkeypatch.setattr(crud, "get_workhours", mock_get_workhours)

    response = test_app.get("/users/999/workhours/")
    assert response.status_code == 404


def test_post_workhour(test_app, monkeypatch):
    test_request_payload = {
        "project_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }
    test_response_payload = {
        "id": 1,
        "user_id": 1,
        "project_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }

    async def mock_post_workhour(*_):
        return 1

    monkeypatch.setattr(crud, "post_workhour", mock_post_workhour)

    response = test_app.post("/users/1/workhours/", json=test_request_payload)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_post_workhour_invalid_json(test_app):
    response = test_app.post("/users/1/workhours/", json={"ame": "test workhour"})
    assert response.status_code == 422


def test_post_workhour_user_not_found(test_app, monkeypatch):
    test_request_payload = {
        "user_id": 999,
        "project_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }

    async def mock_post_workhour(*_):
        return None

    monkeypatch.setattr(crud, "post_workhour", mock_post_workhour)

    response = test_app.post("/users/999/workhours/", json=test_request_payload)

    assert response.status_code == 404
