import requests

from tests.resources.tasks import BASE_URL


def test_read_tasks():
    response = requests.get(BASE_URL + '/tasks')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_read_task():
    response = requests.get(BASE_URL + '/tasks/1')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_create_task():
    response = requests.post(BASE_URL + '/tasks', json={"title": "do homework"})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_completed_task():
    response = requests.put(BASE_URL + '/tasks/1', json={"done": True})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_delete_tasks():
    response = requests.delete(BASE_URL + '/tasks/1')

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'


def test_update_task():
    response = requests.put(BASE_URL + '/tasks/1', json={"title": "buy goods"})

    assert response.status_code == 403
    assert response.json()['error'] == 'Unauthorized access'
