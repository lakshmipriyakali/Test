# testchildclass1.py
import unittest
from childclass1 import ChildClass1

class TestChildClass1(unittest.TestCase):
    def test_multiply(self):
        obj = ChildClass1(5)
        result = obj.multiply(3)
        self.assertEqual(result, 15)
    def test_add(self):
        obj = ChildClass1(5)
        result = obj.add(3)
        self.assertEqual(result, 8)
    def test_subtract(self):
        obj = ChildClass1(5)
        result = obj.subtract(3)
        self.assertEqual(result, 2)