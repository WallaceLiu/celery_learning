#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-02 00:32
@Author:  yuguanquan
@File: wsgi.py
@Software: PyCharm
"""
from flask.cli import load_dotenv
from example.app import init_flask

load_dotenv()
flask_app = init_flask()
