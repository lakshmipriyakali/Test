# test_child_class1.py
import unittest
from childclass2 import ChildClass2

class TestChildClass2(unittest.TestCase):

    def test_calculate_area(self):
        child_class2_instance = ChildClass2(5)  # Provide a value, for example, 5
        result = child_class2_instance.calculate_area(4, 5)
        expected_result = 20
        self.assertEqual(result, expected_result)

    def test_calculate_volume(self):
        child_class2_instance = ChildClass2(5)
        result = child_class2_instance.calculate_volume(2, 3, 4)
        expected_result = 24
        self.assertEqual(result, expected_result)

    def test_compute_perimeter(self):
        child_class2_instance = ChildClass2(5)
        result = child_class2_instance.compute_perimeter(5)
        expected_result = 20
        self.assertEqual(result, expected_result)