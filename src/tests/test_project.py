import json
import pytest

from crud.project import project_crud as crud
from api.model import ProjectDB, WorkhourDB


def test_create_project(test_app, monkeypatch):
    test_request_payload = {
        "name": "test project",
    }
    test_response_payload = {
        "id": 1,
        "name": "test project",
    }

    async def mock_post(*_):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/projects/", json=test_request_payload)

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_project_empty_json(test_app):
    response = test_app.post("/projects/", json={})
    assert response.status_code == 422


def test_create_project_invalid_json(test_app):
    response = test_app.post("/projects/", json={"ame": "test project"})
    assert response.status_code == 422


def test_get_single_project(test_app, monkeypatch):
    test_data = {
        "id": 1,
        "name": "test project",
    }

    async def mock_get(*_):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/projects/1/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_single_project_not_found(test_app, monkeypatch):
    async def mock_get(*_):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/projects/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_get_all_projects(test_app, monkeypatch):
    test_data = [
        {
            "id": 1,
            "name": "test project 1",
        },
        {
            "id": 2,
            "name": "test project 2",
        },
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/projects/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_put_project(test_app, monkeypatch):
    test_request_payload = {
        "id": 1,
        "name": "test project",
    }
    test_crud_payload = {
        "id": 1,
        "name": "test project",
    }
    test_response_payload = {
        "id": 1,
        "name": "test project",
    }

    async def mock_put(*_):
        return test_crud_payload

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/projects/1/", json=test_request_payload)
    assert response.status_code == 200
    assert response.json() == test_response_payload


def test_put_project_not_found(test_app, monkeypatch):
    test_request_payload = {
        "name": "test project",
    }

    async def mock_put(*_):
        return None

    monkeypatch.setattr(crud, "put", mock_put)

    response = test_app.put("/projects/999/", json=test_request_payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_put_project_empty_json(test_app):
    response = test_app.put("/projects/1/", json={})
    assert response.status_code == 422


def test_put_project_invalid_json(test_app):
    response = test_app.put("/projects/1/", json={"ame": "test project"})
    assert response.status_code == 422


def test_delete_project(test_app, monkeypatch):
    async def mock_delete(*_):
        return 1

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/projects/1/")
    assert response.status_code == 200
    assert response.json() == {"detail": "Deleted"}


def test_delete_project_not_found(test_app, monkeypatch):
    async def mock_delete(*_):
        return None

    monkeypatch.setattr(crud, "delete", mock_delete)

    response = test_app.delete("/projects/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_get_workhours(test_app, monkeypatch):
    test_data = [
        {
            "id": 1,
            "project_id": 1,
            "user_id": 1,
            "start_date": "2021-01-01T00:00:00",
            "end_date": "2021-01-01T08:00:00",
        },
        {
            "id": 2,
            "project_id": 1,
            "user_id": 1,
            "start_date": "2021-01-01T08:00:00",
            "end_date": "2021-01-01T16:00:00",
        },
    ]

    async def mock_get_workhours(*_):
        return test_data

    monkeypatch.setattr(crud, "get_workhours", mock_get_workhours)

    response = test_app.get("/projects/1/workhours/")
    assert response.status_code == 200
    assert response.json() == test_data


def test_get_workhours_not_found(test_app, monkeypatch):
    async def mock_get_workhours(*_):
        return None

    monkeypatch.setattr(crud, "get_workhours", mock_get_workhours)

    response = test_app.get("/projects/999/workhours/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"
