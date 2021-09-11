"""

$ celery -A celery_wf_group_state.return.tasks worker --loglevel=info

"""
from celery_wf_group_state_return.tasks import group_task
from time import sleep

if __name__ == '__main__':
    task = group_task.apply_async()
    print('task', task.get())
    # sleep(10)
    #
    # print('apply_async', task.get())
    # task = group_task.AsyncResult(task.task_id)
    # print('AsyncResult', task.get())
