"""数据库的行表示为python对象。
由于数据库有自己的一套结构，所以在操作与行相对应的对象时，我们必须知道这个数据库的结构，
动态行为，可以通过python的__getattr__特殊方法来做"""


class LazyDB(object):
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


# data = LazyDB()
# print('Before:', data.__dict__)
# print('foo:', data.foo)
# print('After:', data.__dict__)


class LoggingLazyDB(LazyDB):  # 给LazyDB添加记录功能，把程序对__getattr__的调用行为记录下来
    def __getattr__(self, name):
        print('Called__getattr__(%s)' % name)
        return super().__getattr__(name)


# data = LoggingLazyDB()
# print('exists:', data.exists)
# print('foo:', data.foo)
# print('foo:', data.foo)


class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value


# data = ValidatingDB()
# print('exists:', data.exists)
# print('foo:', data.foo)
# print('foo:', data.foo)


class BrokenDictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):  # 会导致程序反复递归，从而令其突破最大的栈深度并崩溃
        print('Called __getattribute__(%s)' % name)
        return self._data[name]


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        data_dict = super().__getattribute__('_data')  # 如果要在__getattribute__和__setattr__方法中访问实例属性，那么应该直接
        #  通过super()来做，避免无限递归
        return data_dict[name]




