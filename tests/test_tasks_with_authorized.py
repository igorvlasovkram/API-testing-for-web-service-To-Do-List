from tests.resources import tasks


def test_read_tasks():
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


def test_read_task():
    response, read_task = tasks.read(2)

    assert response.status_code == 200
    assert read_task['title'] == 'Learn Python'
    assert read_task['description'] ==\
           'Need to find a good Python tutorial on the web'
    assert read_task['done'] == False


def test_create_task():
    response, created_task = tasks.create({
        'title': 'do homework',
        'description': 'API testing'
    })
    new_tasks = tasks.read()[1]

    assert response.status_code == 201
    assert new_tasks[0]['title'] == 'Buy groceries'
    assert new_tasks[0]['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert new_tasks[0]['done'] == False
    assert new_tasks[1]['title'] == 'Learn Python'
    assert new_tasks[1]['description'] ==\
           'Need to find a good Python tutorial on the web'
    assert new_tasks[1]['done'] == False
    assert new_tasks[2]['title'] == 'do homework'
    assert new_tasks[2]['description'] == 'API testing'
    assert new_tasks[2]['done'] == False
    assert len(new_tasks) == 3


def test_update_only_one_parameter_of_task():
    response = tasks.put(1, {'title': 'Buy goods'})
    new_tasks = tasks.read()[1]

    assert response.status_code == 200
    assert new_tasks[0]['title'] == 'Buy goods'
    assert new_tasks[0]['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert new_tasks[0]['done'] == False
    assert new_tasks[1]['title'] == 'Learn Python'
    assert new_tasks[1]['description'] ==\
           'Need to find a good Python tutorial on the web'
    assert new_tasks[1]['done'] == False
    assert len(new_tasks) == 2


def test_update_few_parameter_of_task():
    response = tasks.put(
        1,
        {
            'title': 'Buy goods',
            'description': 'Pen, Paper, Paint, Pencil',
            'done': True
        }
    )
    new_tasks = tasks.read()[1]

    assert response.status_code == 200
    assert new_tasks[0]['title'] == 'Buy goods'
    assert new_tasks[0]['description'] == 'Pen, Paper, Paint, Pencil'
    assert new_tasks[0]['done'] == True
    assert new_tasks[1]['title'] == 'Learn Python'
    assert new_tasks[1]['description'] == \
           'Need to find a good Python tutorial on the web'
    assert new_tasks[1]['done'] == False
    assert len(new_tasks) == 2


def test_delete_task():
    response = tasks.delete(2)
    remaining_tasks = tasks.read()[1]

    assert response.status_code == 200
    assert len(remaining_tasks) == 1


def test_delete_all_tasks():
    tasks.delete(1)
    tasks.delete(2)
    remaining_tasks = tasks.read()[1]

    assert len(remaining_tasks) == 0


def test_delete_completed_task():
    tasks.put(1, {'done': True})

    response = tasks.delete(1)

    assert response.status_code == 200
    assert len(tasks.read()[1]) == 1


def test_main_workflow():
    tasks.create({
        'title': 'Do homework',
        'description': 'API testing'
    })

    response, read_tasks = tasks.read()
    assert response.status_code == 200
    assert len(read_tasks) == 3
    assert read_tasks[0]['title'] == 'Buy groceries'
    assert read_tasks[0]['description'] == 'Milk, Cheese, Pizza, Fruit, Tylenol'
    assert read_tasks[0]['done'] == False
    assert read_tasks[1]['title'] == 'Learn Python'
    assert read_tasks[1]['description'] == \
           'Need to find a good Python tutorial on the web'
    assert read_tasks[1]['done'] == False
    assert read_tasks[2]['title'] == 'Do homework'
    assert read_tasks[2]['description'] == 'API testing'
    assert read_tasks[2]['done'] == False

    response = tasks.put(3, {'title': 'Do homework #9'})
    assert response.status_code == 200
    assert tasks.read(3)[1]['title'] == 'Do homework #9'

    response = tasks.put(3, {'done': True})
    assert response.status_code == 200
    assert tasks.read(3)[1]['done'] == True

    response = tasks.delete(3)
    assert response.status_code == 200
    assert len(tasks.read()[1]) == 2
