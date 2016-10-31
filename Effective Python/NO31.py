from weakref import WeakKeyDictionary


class HomeWork(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = HomeWork()
galileo.grade = 95


# class Exam(object):
#     def __init__(self):
#         self._writing_grade = 0
#         self._math_grade = 0
#
#     @staticmethod
#     def _check_grade(value):
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')


# class Grade(object):
#     def __get__(*args, **kwargs):
#
#     def __set__(*args, **kwargs):


# class Grade(object):
#     def __init__(self):
#         self._value = 0
#
#     def __get__(self, instance, owner):
#         return self._value
#
#     def __set__(self, instance, value):
#         if not (0 <= value <= 100):
#             raise ValueError('Grade must be between 0 and 100')
#         self._value = value
#
#
# class Exam(object):
#     math_grade = Grade()
#     writing_grade = Grade()
#     science_grade = Grade()
#
#
# first_exam = Exam()
# first_exam.writing_grade = 82
# first_exam.science_grade = 99
# print('Writing', first_exam.writing_grade)
# print('Science', first_exam.science_grade)
#
# second_exam = Exam()
# second_exam.writing_grade = 75
# print('Second', second_exam.writing_grade, 'is right')
# print('First', first_exam.writing_grade, 'is wrong')


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


