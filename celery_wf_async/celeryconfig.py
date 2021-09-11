import os

BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 43200}
CELERY_IMPORTS = ('tasks',)
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
# uncomment to enable debugging:
CELERYD_POOL = 'celery.concurrency.threads:TaskPool'
