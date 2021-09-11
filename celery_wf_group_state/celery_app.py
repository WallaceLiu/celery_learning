# from celery_once import QueueOnce
from celery import Celery

CELERY_BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app = Celery('celery_wf_group_state', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
