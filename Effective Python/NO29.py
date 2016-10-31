"""元类：能够定制其他类的类，又称为描述类，可以把python的class语句转译为元类，并令其在每次定义具体的类时，都提供独特的行为"""


# class OldResistor(object):
#     def __init__(self, ohms):
#         self._ohms = ohms
#
#     def get_ohms(self):
#         return self._ohms
#
#     def set_ohms(self, ohms):
#         self._ohms = ohms
#
#
# r0 = OldResistor(50e3)
# print('Before: %5r' % r0.get_ohms())
# r0.set_ohms(10e3)
# print('After: %5r' % r0.get_ohms())


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


# r1 = Resistor(50e3)
# print(r1.ohms)
# r1.ohms = 10e3
# print(r1.ohms)
# r1.ohms += 5e3
# print(r1.ohms)


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property  # getter方法
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


# r2 = VoltageResistance(1e3)
# print('Before: %5r amps' % r2.current)
# r2.voltage = 10
# print('After: %5r amps' % r2.current)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


# r3 = BoundedResistance(1e3)
# r3.ohms = 0


class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

# r4 = FixedResistance(1e3)
# r4.ohms = 2e3


class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current  # 不要在getter中修改属性
        return self._ohms


# r7 = MysteriousResistor(10)
# r7.current = 0.01
# print('Before: %5r' % r7.voltage)
# r7.ohms
# print('After: %5r' % r7.voltage)


