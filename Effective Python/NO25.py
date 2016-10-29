#! python3
# -*- coding: utf-8 -*-
from pprint import pprint


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):  # 初始化父类的传统方式,如果子类受到了多重继承的影响，这种方式就不好了
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# foo = OneWay(5)
# print('First ordering is (5*2)+5=', foo.value)


class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# bar = AnotherWay(5)
# print('Second ordering still is', bar.value)


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

# foo = ThisWay(5)
# print('Should be (5*5)+2=27 but is', foo.value)


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


# foo = GoodWay(5)
# print('Should be 5*(5+2)=35 and is', foo.value)
# pprint(GoodWay.mro())


class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value*2)  # python3语法


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value*2)

assert Explicit(10).value == Implicit(10).value