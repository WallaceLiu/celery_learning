from __future__ import absolute_import
from celery_chrod import celery_app
from celery import chord


@celery_app.task(name='celery_chrod.add')
def add(x, y):
    return x + y


@celery_app.task(name='celery_chrod.tsum')
def tsum(numbers):
    return sum(numbers)


if __name__ == '__main__':
    tasks = [add.s(100, 100), add.s(200, 200)]
    # chord(tasks, tsum.s()).apply_async()
    result = chord(header)(callback)
    chord(tasks)(tsum.s())
