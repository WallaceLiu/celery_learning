"""

$ celery -A celery_wf_group.tasks worker --loglevel=info

"""
from __future__ import absolute_import, unicode_literals, print_function
from celery import Celery

import os
import time

CELERY_BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('celery_wf_group', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def mul(x, y):
    time.sleep(5)
    return x * y


@app.task
def less(x, y):
    time.sleep(5)
    return x - y


@app.task
def exc(x, y):
    time.sleep(5)
    return x / y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def temp():
    return [xsum(range(10)), xsum(range(100))]


@app.task
def temp1():
    return [add(i, i) for i in range(10)]


@app.task
def tsum(numbers):
    return sum(numbers)


@app.task
def log_error(request, exc, traceback):
    with open(os.path.join('/var/errors', request.id), 'a') as fh:
        print('--\n\n{0} {1} {2}'.format('task_id', exc, traceback), file=fh)


@app.task
def on_chord_error(request, exc, traceback):
    print('Task {0!r} raised error: {1!r}'.format(request.id, exc))
