#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 20:15
@Author:  yuguanquan
@File: extensions.py
@Software: PyCharm
"""
from celery import Celery
from flask import Flask
from example import config

flask_app = Flask(config.flask_import_name)
celery_app = Celery()
