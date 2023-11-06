# module2.py
from my_package.module1 import Dog

class Beagle(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def description(self):
        return f"{self.name} is a Beagle, aged {self.age} years."
