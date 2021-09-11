BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_IMPORTS = (
    "canvas_kaboom.chord_chain",
    "canvas_kaboom.group_upgrades",
)
CELERY_RESULT_BACKEND = "redis://localhost/1"
