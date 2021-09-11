from __future__ import absolute_import
from celery import Celery

CELERY_BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('sophie',
             broker=CELERY_BROKER_URL,
             backend=CELERY_RESULT_BACKEND,
             include=['celery_chrod.chord_test'])

app.conf.update(
    CELERY_ACCEPT_CONTENT=["json"],
    CELERY_TASK_SERIALIZER="json",
    CELERY_TRACK_STARTED=True,
    CELERYD_PREFETCH_MULTIPLIER=1,  # NO PREFETCHING OF TASKS
    BROKER_TRANSPORT_OPTIONS={
        'priority_steps': [0, 1]  # ALLOW ONLY 2 TASK PRIORITIES
    }
)

if __name__ == '__main__':
    app.start()
