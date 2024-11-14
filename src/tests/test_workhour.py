import json
import pytest

from crud.workhour import workhour_crud as crud
from api.model import WorkhourDB, ProjectDB, UserDB


def test_put_workhour(test_app, monkeypatch):
    test_request_payload = {
        "id": 1,
        "project_id": 1,
        "user_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }
    test_crud_payload = {
        "id": 1,
        "project_id": 1,
        "user_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }
    test_response_payload = {
        "id": 1,
        "project_id": 1,
        "user_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }

    async def mock_put(*_):
        return test_crud_payload

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/workhours/1/", json=test_request_payload)
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_put_workhour_not_found(test_app, monkeypatch):
    test_request_payload = {
        "project_id": 1,
        "user_id": 1,
        "start_date": "2021-01-01T00:00:00",
        "end_date": "2021-01-01T08:00:00",
    }

    async def mock_put(*_):
        return None

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/workhours/999/", json=test_request_payload)
    assert response.status_code == 404


def test_delete_workhour(test_app, monkeypatch):
    async def mock_delete(*_):
        return 1

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/workhours/1/")
    assert response.status_code == 200
    assert response.json() == {"detail": "Deleted"}


def test_delete_workhour_not_found(test_app, monkeypatch):
    async def mock_delete(*_):
        return None

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/workhours/999/")
    assert response.status_code == 404


def test_get_user(test_app, monkeypatch):
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

    async def mock_get_user(*_):
        return test_crud_payload

    monkeypatch.setattr(crud, "get_user", mock_get_user)

    response = test_app.get("/workhours/1/user/")

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_user_not_found(test_app, monkeypatch):
    async def mock_get_user(*_):
        return None

    monkeypatch.setattr(crud, "get_user", mock_get_user)

    response = test_app.get("/workhours/999/user/")
    assert response.status_code == 404


def test_get_project(test_app, monkeypatch):
    test_response_payload = {
        "id": 1,
        "name": "test project",
    }

    async def mock_get_project(*_):
        return test_response_payload

    monkeypatch.setattr(crud, "get_project", mock_get_project)

    response = test_app.get("/workhours/1/project/")

    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_get_project_not_found(test_app, monkeypatch):
    async def mock_get_project(*_):
        return None

    monkeypatch.setattr(crud, "get_project", mock_get_project)

    response = test_app.get("/workhours/999/project/")
    assert response.status_code == 404
