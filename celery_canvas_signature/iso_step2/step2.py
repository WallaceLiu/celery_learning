from celery import Celery
import logging
from .settings import broker, backend

app = Celery('step2',
             broker=broker,
             backend=backend)

app.config_from_object('celery_config')


@app.task
def s2(x, y):
    return x * y
