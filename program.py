# pip install -U "celery[redis]"
# pip install flower
# pip install eventlet
# pip install pylint autopep8

# https://www.distributedpython.com/2018/05/29/task-routing/
# https://www.distributedpython.com/2018/05/15/testing-celery-chains/

# cd ~/Desktop/celery_proj/test
# celery -A tasks worker --loglevel=INFO --concurrency=1 -n worker1 --queues=queue1
# celery -A tasks worker --loglevel=INFO --concurrency=1 -n worker2 --queues=queue2
# flower -A tasks

# run through eventlet
# celery -A tasks worker -l INFO --concurrency=500 --pool=eventlet -n worker1 --queues=queue1
# celery -A tasks worker -l INFO --concurrency=500 --pool=eventlet -n worker2 --queues=queue2

# cd ~/Desktop/celery_proj
# python program.py

# NOTES:
"""
Program sends all the add func tasks to queue1 queue & all the subtract func tasks to queue2 queue.

https://docs.celeryproject.org/en/stable/userguide/concurrency/eventlet.html
To mock heavy I/O tasks, time.sleep is used in tasks and the same when tun through prefork pool i.e.
celery -A tasks worker --loglevel=INFO --concurrency=2 -n worker1 --queues=queue1
is very slow, since max 2 concurrency is possible.
But when the workers are run through eventlet with concurrency=500, it executes in parallel.
"""

import time

from test.tasks import add, subtract  # noqa


if __name__ == '__main__':
    print('Hello')

    for i in range(10):
        # time.sleep(2)
        add.delay(3, 1)
        subtract.delay(3, 1)
