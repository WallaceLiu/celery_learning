 #!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 19:35
@Author:  yuguanquan
@File: celery_app.py
@Software: PyCharm
"""
from flask.cli import  load_dotenv
from example.app import init_celery

load_dotenv()
celery_app = init_celery()


