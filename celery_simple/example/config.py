#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 19:24
@Author:  yuguanquan
@File: config.py
@Software: PyCharm
"""
import os

flask_import_name = 'example'
worker_concurrency = 5
result_backend = os.getenv('CELERY_RESULT_BACKEND_URL')
broker_url = os.getenv("CELERY_BROKER_URL")