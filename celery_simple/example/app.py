#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 19:05
@Author:  yuguanquan
@File: app.py
@Software: PyCharm
"""

from werkzeug.utils import import_string
from flask import jsonify
from example import api
from flask import request
from example.extensions import *
from datetime import timedelta


def init_flask(testing=False, cli=False):
    app = flask_app
    app.config.update(read_config())
    init_celery(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    @app.errorhandler(404)
    def page_not_found(_):
        return jsonify({'code': 404, 'message': f'page {request.base_url} not found'})

    @app.errorhandler(500)
    def internal_error(_):
        return jsonify({'code': 500, 'message': 'internal code error'})

    app.register_blueprint(api.test.blueprint)


def init_celery(app: Flask = None):
    app = app or init_flask()
    celery_app.conf.beat_schedule = {
        'test-schedule': {
            'task': 'simple.tasks.test.test_schedule',
            'schedule': timedelta(seconds=5),
        },
    }
    celery_app.conf.update(app.config)
    import psutil
    celery_max_mem_kilobytes = (psutil.virtual_memory().total * 0.85) / 1024
    celery_app.conf.worker_max_memory_per_child = int(celery_max_mem_kilobytes / celery_app.conf.worker_concurrency)

    class ContextTask(celery_app.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app


def read_config():
    result_dict = dict()
    obj = import_string('example.config')
    for key in dir(obj):
        result_dict[key] = getattr(obj, key)
    return result_dict
