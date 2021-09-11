#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Jervon
@contact: jervon@foxmail.com
@time: 2018/4/23 上午9:51
"""

from celery_long_task_tornado.handler.wsv2 import wsVersionTwoHandler
from celery_long_task_tornado.handler.server_sendee import ServerSendeeHandler, CeleryTaskDoneHandler

urls = [
    (r"/ws/v2/", wsVersionTwoHandler),
    (r"/service_sendee/", ServerSendeeHandler),
    (r"/celery_task_done/", CeleryTaskDoneHandler),
]
