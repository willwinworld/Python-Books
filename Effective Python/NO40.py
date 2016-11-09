#! python3
# -*- coding: utf-8 -*-
from collections import namedtuple


def my_coroutine():
    while True:
        received = yield
        print('Received:', received)


it = my_coroutine()
next(it)
it.send('First')
it.send('Second')


def minimize():
    current = yield   # 把外界传进来的首个值，当成目前的最小值
    while True:
        value = yield current  # 生成器会屡次执行while循环中那条yield语句，以便将当前统计的最小值告诉外界
        current = min(value, current)


it = minimize()
next(it)
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))


Query = namedtuple('Query', ('y', 'x'))
