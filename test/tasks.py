import time

from celery import Celery

app = Celery('tasks', broker='redis://')

app.conf.update({
    'task_routes': {
        'add': {'queue': 'queue1'},
        'subtract': {'queue': 'queue2'}
    }
})


@app.task(name='add')
def add(x, y):
    time.sleep(10)
    return x + y


@app.task(name='subtract')
def subtract(x, y):
    time.sleep(20)
    return x - y
