import os
import pytest
import app
import database

TEST_DB = "test_todo.db"


@pytest.fixture
def client():
    database.DATABASE_NAME = TEST_DB

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    database.create_table()

    with app.app.test_client() as client:
        yield client

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do App" in response.data


def test_add_task(client):
    client.post("/", data={"task": "Test Task"})
    response = client.get("/")
    assert b"Test Task" in response.data


def test_update_task(client):
    client.post("/", data={"task": "Old Task"})
    task_id = database.get_all_tasks()[0]["id"]

    client.post(f"/update/{task_id}", data={"new_task": "New Task"})
    response = client.get("/")

    assert b"New Task" in response.data
    assert b"Old Task" not in response.data


def test_complete_task(client):
    client.post("/", data={"task": "Complete Me"})
    task_id = database.get_all_tasks()[0]["id"]

    client.get(f"/complete/{task_id}")
    response = client.get("/")

    assert b"Completed" in response.data


def test_delete_task(client):
    client.post("/", data={"task": "Delete Me"})
    task_id = database.get_all_tasks()[0]["id"]

    client.get(f"/delete/{task_id}")
    response = client.get("/")

    assert b"Delete Me" not in response.data
