from tests.resources import tasks

BASE_URL = 'http://localhost:5000/todo/api/v1.0'


def test_unauthorized_read_tasks():
    response = tasks.read()[0]

    assert response.status_code != 200
    assert response.json()['error'] == 'Unauthorized access'


def test_authorized_read_tasks():
    response, read_tasks = tasks.read()

    assert response.status_code == 200
    assert len(read_tasks) == 3
    assert read_tasks[0] == 'Buy groceries'


def test_authorized_create_task():
    response, created_task = tasks.create({"title": "do homework"})

    assert response.status_code == 201
    assert created_task['title'] == 'do homework'
    assert created_task['description'] == ''
    assert created_task['done'] == False


def test_e2e_authorized_create_task():
    original_tasks = tasks.read()

    response, created_task = tasks.create({"title": "do homework"})

    assert response.status_code == 201
    assert created_task['title'] == 'do homework'
    assert created_task['description'] == ''
    assert created_task['done'] == False

    new_task = tasks.read()

    assert len(new_task) == len(original_tasks) + 1
