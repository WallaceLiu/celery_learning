"""

$ celery -A celery_wf_group_state_return.tasks worker --loglevel=info

"""
import logging

from celery_wf_group_state.celery_app import app
from celery import group
from celery.result import allow_join_result
from time import sleep
import random
import time

# on_message回调值传递组任务内的任务进度, 更新组任务的进度需要获取group task对象
task_obj = None
# on_message回调每次只会返回一个子任务的任务进度, 做个全局进度保存
task_status = {
    'task_A': {
        'status': 'PROGRESS',
        'current': 0,
        'progress': 0,
        'total': 0,
        'msg': '',
    },
    'task_B': {
        'status': 'PROGRESS',
        'current': 0,
        'progress': 0,
        'total': 0,
        'msg': '',
    },
}


def progress_update(meta_data):
    """
    更新进度的回调函数

    {'task_name': "task_B",
     'current': i,
     'total': total,
     'progress': i,
     'state': message,
     'status': "progress"}

    :param meta_data: 回调会自动获取任务反馈的进度meta_data
    :return: None
    """
    global task_obj
    global task_status

    logging.info("meta,meta,meta: {}".format(meta_data))

    meta_data_result = meta_data["result"]
    task_name = meta_data_result["task_name"]

    logging.info("task_name: {}".format(task_name))

    task_status[task_name]["status"] = meta_data_result.get("status")
    task_status[task_name]["current"] = meta_data_result.get("current")
    task_status[task_name]["progress"] = meta_data_result.get("progress")
    task_status[task_name]["total"] = meta_data_result.get("total")
    task_status[task_name]["msg"] = meta_data_result.get("msg")

    if task_status["task_A"]["status"] in ("FINISH", 'SUCCESS') \
            and task_status["task_B"]["status"] in ("FINISH", 'SUCCESS'):
        group_status = "FINISH"
    elif task_status["task_A"]["status"] in ("FAILED") or \
            task_status["task_B"]["status"] in ("FAILED"):
        group_status = "FAILED"
    else:
        group_status = "FINISH"
    #
    if meta_data.get("status") == "FINISH":
        task_status[meta_data_result["task_name"]]["progress"] = meta_data_result["progress"]
    if task_obj:
        logging.info("progress update, task_status: {}".format(task_status))
        task_obj.update_state(state=group_status, meta_data=dict(**task_status))
    else:
        logging.error("can't get global task_obj!")


@app.task(bind=True)
def group_task(self):
    """
    - 将被拆分的组任务，拆成以下两个子任务：
      - task_A
      - task_B
    """
    # 更新全局变量task_obj为当前组任务
    global task_obj
    task_obj = self

    group_task_id = self.request.id
    # 创建组任务
    res = group(A.si(0, 0),
                B.si(0, 0))()

    with allow_join_result():
        result = res.get(on_message=progress_update, propagate=False)
    logging.info("group task finish.")
    logging.info(result)
    return {'current': 2, 'total': 2, 'status': 'Task completed!',
            'result': result}


@app.task(bind=True)
def A(self, x, y):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'task_name': "task_A",
                                'current': i,
                                'progress': i,
                                'total': total,
                                'status': "PROGRESS",
                                'msg': message})
        time.sleep(1)
    return {'current': total, 'progress': total, 'total': total, 'status': 'FINISH',
            'result': 42, 'task_name': "task_A"}


@app.task(bind=True)
def B(self, x, y):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(100, 140)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'task_name': "task_B",
                                'current': i,
                                'progress': i,
                                'total': total,
                                'status': "PROGRESS",
                                'msg': message})
        time.sleep(1)
    return {'current': total, 'progress': total, 'total': total, 'status': 'FINISH',
            'result': 42, 'task_name': "task_B"}
