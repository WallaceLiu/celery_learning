#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021-01-01 19:32
@Author:  yuguanquan
@File: views.py
@Software: PyCharm
"""
from flask.blueprints import Blueprint
from flask import jsonify
from celery.result import AsyncResult
from simple.tasks import test

blueprint = Blueprint('test', __name__, url_prefix='/test/v1')


@blueprint.route('/async_task', methods=['GET'])
def async_task_view():
    print('async_task')
    async_result: AsyncResult = test.async_task.apply_async()
    print(async_result.task_id)
    return jsonify({'code': 0, 'message': 'success', 'data': {'taskId': async_result.task_id}})
