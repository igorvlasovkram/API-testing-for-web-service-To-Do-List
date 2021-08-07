import pytest
import requests


@pytest.fixture(scope='function', autouse=True)
def store_managment():
    yield
    requests.post('http://localhost:5000/todo/api/v1.0/origin_tasks')
