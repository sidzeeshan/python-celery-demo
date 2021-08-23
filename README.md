# python-celery-demo

# pip install -U "celery[redis]"
# pip install flower eventlet

# celery -A tasks worker --loglevel=INFO --concurrency=1 -n worker1 --queues=queue1
# celery -A tasks worker --loglevel=INFO --concurrency=1 -n worker2 --queues=queue2
# flower -A tasks

# run through eventlet
# celery -A tasks worker -l INFO --concurrency=500 --pool=eventlet -n worker1 --queues=queue1
# celery -A tasks worker -l INFO --concurrency=500 --pool=eventlet -n worker2 --queues=queue2

# cd celery_proj
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
