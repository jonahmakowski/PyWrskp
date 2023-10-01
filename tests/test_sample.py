# testing sample
from src.testing_sample import main as my_module
import unittest

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(my_module.add(2, 3), 5)  # Test the 'add' function

    def test_subtract(self):
        self.assertEqual(my_module.subtract(5, 2), 3)  # Test the 'subtract' function

if __name__ == '__main__':
    unittest.main()
