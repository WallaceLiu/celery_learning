"""
This modules initializes Celery and does some configurations
"""
from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost',
             include=['tasks'])
accept_content = {
    'CELERY_ACCEPT_CONTENT': ['pickle', 'application/json', 'msgpack', 'yaml']
}
app.conf.update(accept_content)
