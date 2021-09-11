#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 19:34
@Author:  yuguanquan
@File: test.py
@Software: PyCharm
"""

from example.extensions import celery_app


@celery_app.task
def async_task():
    print('async_task_task')
