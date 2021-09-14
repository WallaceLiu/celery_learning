from celery import Celery

from .settings import broker, backend

app = Celery('step1',
             broker=broker,
             backend=backend,
             tasks=[])

app.config_from_object('celery_config')


@app.task
def s1(x, y):
    return x + y
