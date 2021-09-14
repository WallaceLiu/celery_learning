from . import app
from celery.canvas import group


@app.task
def gu_produce_n(n):
    print('Producing', n)
    return n


@app.task
def gu_collect_total(ns):
    print('Collecting', ns)
    return sum(ns)


@app.task
def gu_print_result(total):
    print('Resulted', total)
    return total


def gu_works():
    return (group([gu_produce_n.s(n + 1) for n in range(10)]) | (gu_collect_total.s() | gu_print_result.s())
            )()
