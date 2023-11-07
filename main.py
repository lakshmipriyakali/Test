from childclass1 import ChildClass1
from childclass2 import ChildClass2

obj1 = ChildClass1(5)
print(obj1.get_value())  # Should print 5
print(obj1.multiply(3))  # Should print 15

obj2 = ChildClass2(10)
print(obj2.get_value())  # Should print 10
print(obj2.calculate_area(4, 5))  # Should print 20

# Import test modules and run the tests
import unittest
from testchildclass1 import TestChildClass1
from testchildclass2 import TestChildClass2

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestChildClass1)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestChildClass2)
    unittest.TextTestRunner(verbosity=2).run(suite)
