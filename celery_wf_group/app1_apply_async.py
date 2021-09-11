from celery_wf_group.tasks import add
from celery import group

if __name__ == '__main__':
    for i in range(5):
        t = add.apply_async(args=(i, i))
        print(t.task_id, t.get())
        r = add.AsyncResult(t.task_id)
        # AsyncResult 的返回值
        # statue是任务状态，info是add方法的return值
        print(r, r.state, r.info, r.get())
