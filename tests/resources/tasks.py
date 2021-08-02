import requests


BASE_URL = 'http://localhost:5000/todo/api/v1.0'


def authorized(resource_url, json=None) -> dict:
    return dict(
        url=BASE_URL + resource_url,
        auth=('miguel', 'python'),
        json=json
    )


def read(task_id: str = '') -> tuple:
    if task_id == '':
        response = requests.get(**authorized('/tasks'))
        return response, response.json()['tasks']
    else:
        response = requests.get(**authorized('/tasks' + '/' + task_id))
        return response, response.json()['task']


def create(task: dict) -> tuple:
    response = requests.post(**authorized(
        '/tasks',
        json=task
    ))
    return response, response.json()['task']
