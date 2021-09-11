FLASK_ENV=development
FLASK_APP=simple.app:create_app
FLASK_RUN_PORT=5000
CELERY_BROKER_URL=amqp://guest:guest@127.0.0.1:5672//
CELERY_RESULT_BACKEND_URL=redis://127.0.0.1/2
