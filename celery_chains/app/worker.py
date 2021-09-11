import os
from celery import Celery

CELERY_BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery(__name__)
app.conf.update({
    'broker_url': CELERY_BROKER_URL,
    'result_backend': CELERY_RESULT_BACKEND,
    'imports': (
        'tasks',
    ),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']
})
