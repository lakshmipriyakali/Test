# child_class2.py
from parentclass import ParentClass

class ChildClass2(ParentClass):
    def calculate_area(self, width, height):
        return width * height

    def calculate_volume(self, length, width, height):
        return length * width * height

    def compute_perimeter(self, side_length):
        return 4 * side_length
