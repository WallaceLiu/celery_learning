from celery import Celery, chain

from .settings import backend, broker

app = Celery('demo', broker=broker, backend=backend)
app.config_from_object('celery_config')
s1 = app.signature('step1.s1', args=(1,))
s2 = app.signature('step2.s2', args=(2,))
s3 = (s1 | s2)
res = s3.apply_async((4,))

print(res.get(5))
