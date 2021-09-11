from . import app
from celery.canvas import chord


@app.task
def cc_produce_n(n):
    print('Producing', n)
    return n


@app.task
def cc_collect_total(ns):
    print('Collecting', ns)
    return sum(ns)


@app.task
def cc_print_result(total):
    print('Resulted', total)
    return total


def cc_fails():
    return (
        chord([
            cc_produce_n.s(n + 1) for n in range(10)
        ])(
            cc_collect_total.s() | \
            cc_print_result.s()
        )
    )


def cc_works():
    return (
        chord([
            cc_produce_n.s(n + 1) for n in range(10)
        ])(
            cc_collect_total.s()
        )
    )
