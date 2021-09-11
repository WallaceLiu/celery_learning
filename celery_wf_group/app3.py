from celery_wf_group.tasks import add, less, mul, exc
from celery import group

if __name__ == '__main__':
    for i in range(10):
        res_add = add.delay(i, i)
        print(res_add.get())

        res_less = less.delay(10, i)
        print(res_less.get())

        res_mul = mul.delay(i, i)
        print(res_mul.get())

        res_exc = exc.delay(i, 10)
        print(res_exc.get())
