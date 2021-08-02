import requests

from tests.resources import tasks
from tests.resources.tasks import BASE_URL


def test_unauthorized_read_tasks():
    response = requests.get(BASE_URL + '/tasks')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_unauthorized_read_task():
    response = requests.get(BASE_URL + '/tasks/1')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_unauthorized_create_task():
    response = requests.post(BASE_URL + '/tasks', json={"title": "do homework"})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_unauthorized_completed_task():
    response = requests.put(BASE_URL + '/tasks/1', json={"done": True})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_unauthorized_delete_tasks():
    response = requests.delete(BASE_URL + '/tasks/1')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_unathorized_update_task():
    response = requests.put(BASE_URL + '/tasks/1', json={"title": "buy goods"})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_authorized_read_tasks():
    response, read_tasks = tasks.read()

    assert response.status_code == 200
    assert len(read_tasks) == 2
    assert read_tasks[0]['title'] == 'Buy groceries'
    assert read_tasks[0]['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert read_tasks[0]['done'] == False
    assert read_tasks[1]['title'] == 'Learn Python'
    assert read_tasks[1]['description'] ==\
           'Need to find a good Python tutorial on the web'
    assert read_tasks[1]['done'] == False


def test_authorized_read_task():
    response, read_task = tasks.read('2')

    assert response.status_code == 200
    assert read_task['title'] == 'Learn Python'
    assert read_task['description'] ==\
           'Need to find a good Python tutorial on the web'
    assert read_task['done'] == False


def test_authorized_create_task():
    response, created_task = tasks.create({"title": "do homework"})

    new_tasks = tasks.read()[1]

    assert response.status_code == 201
    assert created_task['title'] == 'do homework'
    assert created_task['description'] == ''
    assert created_task['done'] == False
    assert len(new_tasks) == 3


def test_authorized_update_task():
    response = requests.put(BASE_URL + '/tasks/2')

    new_tasks = tasks.read()[1]
    new_task = tasks.read('1')[1]

    assert response.status_code == 200
    assert new_task['title'] == 'buy goods'
    assert new_task['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert new_task['done'] == False


def test_e2e_authorized_create_task():
    original_tasks = tasks.read()

    response, created_task = tasks.create({"title": "do homework"})

    assert response.status_code == 201
    assert created_task['title'] == 'do homework'
    assert created_task['description'] == ''
    assert created_task['done'] == False

    new_task = tasks.read()[1]

    assert len(new_task) == len(original_tasks) + 1
