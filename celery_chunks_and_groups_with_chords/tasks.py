"""
This module contains Celery tasks
"""
from celery_chunks_and_groups_with_chords.celery_app import app
from celery_chunks_and_groups_with_chords.constants import LOOP_RANGE


@app.task
def group_task(_id):
    for x in range(LOOP_RANGE):
        print("in loop %d" % _id)
        pass
    print("loop for %d" % _id)
    return _id


@app.task
def callback(*args):
    for task in args:
        print("each task size:%s" % len(task))
    # print "callback kamal args=%r" % args
