# child_class1.py
from parentclass import ParentClass

class ChildClass1(ParentClass):
    def multiply(self, factor):
        return self.value * factor
    def add(self, number):
        return self.value + number
    def subtract(self, number):
        return self.value - number