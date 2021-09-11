#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/5/10 下午4:27
"""

from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
import datetime, time
from celery_long_task_tornado.celery_service.proj import *
from celery_long_task_tornado.celery_service.proj.base_task import BaseTask

logger = get_task_logger(__name__)


@app.task(name='proj.tasks.test_01', base=BaseTask, bind=True)
def test_01(self, a, b):
    # 处理代码
    print("任务处理中...")
    return a + b
