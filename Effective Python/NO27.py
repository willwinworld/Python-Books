#! python3
# -*- coding: utf-8 -*-


# class MyObject(object):
#     def __init__(self):
#         self.public_field = 5
#         self.__private_field = 10
#
#     def get_private_field(self):
#         return self.__private_field
#
#
# foo = MyObject()
# assert foo.public_field == 5
# assert foo.get_private_field() == 10


# def get_no_of_instances(cls_obj):  # 为了仅仅与类交互而不是和实例交互
#     return cls_obj.no_inst
#
#
# class Kls(object):
#     no_inst = 0
#
#     def __init__(self):
#         Kls.no_inst += 1


# ik1 = Kls()
# ik2 = Kls()
# print(get_no_of_instances(Kls))


# def iget_no_of_instance(ins_obj):  # 只在类中运行而不在实例中运行的方法, 想让方法不再实例中运行
#     return ins_obj.__class__.no_inst
#
#
# class Kls(object):
#     no_inst = 0
#
#     def __init__(self):
#         Kls.no_inst += 1
#
# ik1 = Kls()
# ik2 = Kls()
# print(iget_no_of_instance(ik1))


# class Kls(object):
#     no_inst = 0
#
#     def __init__(self):
#         Kls.no_inst += 1
#
#     @classmethod
#     def get_no_of_instance(cls):
#         return cls.no_inst
#
#
# ik1 = Kls()
# ik2 = Kls()
# print(ik1.get_no_of_instance())  # 这样的好处是:不管这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来
# print(Kls.get_no_of_instance())
#
#
# class Data(object):
#     day = 0
#     month = 0
#     year = 0
#
#     def __init__(self, year=0, month=0, day=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def get_date(cls, data_as_string):
#         year, month, day = map(int, data_as_string.split('-'))
#         output = cls(year, month, day)
#         return output
#
#     def out_date(self):
#         print("year: ")
#         print(self.year)
#         print("month: ")
#         print(self.month)
#         print("day: ")
#         print(self.day)
#
# r = Data.get_date("2016-8-6")  # classmethod装饰的没有与实例交互，直接用类调用
# r.out_date()


# class MyOtherObject(object):
#     def __init__(self):
#         self.__private_field = 71
#
#     @classmethod
#     def get_private_field_of_instance(cls, instance):
#         return instance.__private_field
#
#
# bar = MyOtherObject()
# assert MyOtherObject.get_private_field_of_instance(bar) == 71
#
#
# class MyParentObject(object):
#     def __init__(self):
#         self.__private_field = 71
#
#
# class MyChildObject(MyParentObject):
#     def get_private_field(self):
#         return self.__private_field
#
#
# baz = MyChildObject()
# assert baz._MyParentObject__private_field == 71
# print(baz.__dict__)


# class ApiClass(object):
#     def __init__(self):
#         self._value = 5
#
#     def get(self):
#         return self._value
#
#
# class Child(ApiClass):
#     def __init__(self):
#         super(Child, self).__init__()
#         self._value = 'hello'
#
# a = Child()
# print(a.get())

class ApiClass(object):
    def __init__(self):
        self.__value = 5

    def get(self):
        return self.__value


class Child(ApiClass):
    def __init__(self):
        super(Child, self).__init__()
        self._value = 'hello'


a = Child()
print(a.get(), a._value)
