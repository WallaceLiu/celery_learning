##启动命令
> celery启动：venv/bin/celery flower -A example.celery_app:celery_app

> flower监控平台启动：venv/bin/celery flower -A example.celery_app:celery_app

> flask启动：venv/bin/gunicorn example.wsgi:flask_app --workers=1 -b 0.0.0.0:5000

## 注意事项

> Broker建议使用RabbitMQ消息消费的可靠性

> Result Backend 建议使用Redis保证数据存取的可靠性
