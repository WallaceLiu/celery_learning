"""

"""
from celery_wf_group.tasks import add
from celery import group

if __name__ == '__main__':
    gtask = group(add.s(i, i) for i in range(10))()  # add.s
    print(gtask.get())
    print('gtask', gtask)
    print('gtask.task_id', gtask)
