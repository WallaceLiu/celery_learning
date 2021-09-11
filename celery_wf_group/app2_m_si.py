"""

"""
from celery_wf_group.tasks import add
from celery import group

if __name__ == '__main__':
    res = group(add.si(i, i) for i in range(10))()  # add.si
    print(res.get())
