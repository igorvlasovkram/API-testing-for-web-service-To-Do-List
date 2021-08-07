import requests

BASE_URL = 'http://localhost:5000/todo/api/v1.0'


def authorized(resource_url, json=None) -> dict:
    return dict(
        url=BASE_URL + resource_url,
        auth=('miguel', 'python'),
        json=json
    )


def read(task_id: int = None) -> tuple:
    if task_id:
        response = requests.get(**authorized('/tasks' + '/' + str(task_id)))
        return response, response.json()['task']
    else:
        response = requests.get(**authorized('/tasks'))
        return response, response.json()['tasks']


def create(task: dict) -> tuple:
    response = requests.post(**authorized(
        '/tasks',
        json=task
    ))
    return response, response.json()['task']


def delete(tasks_id: int):
    return requests.delete(**authorized('/tasks' + '/' + str(tasks_id)))


def put(tasks_id: int, new_param: dict):
    return requests\
        .put(**authorized('/tasks' + '/' + str(tasks_id), json=new_param))
