"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""
import unittest
import unittest.mock as mock
from mainFolder import main_class_example as main_test

PI = 3.14159265358979323

class MyTestCase(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(main_test.hello_world(), None)

    def test_call_with_value(self):
        self.assertEqual(main_test.PI, main_test.get_pi(True))

    def test_one_input_mock(self):
        #notice this line is different
        with mock.patch('builtins.input', return_value="turtle"):
            self.assertEqual("turtle", main_test.get_user_input_once())

    def test_multiple_input_mock(self):
        #notice this line is different
        with mock.patch('builtins.input', side_effect=["turtle", "penguin"]):
            self.assertEqual("You input turtle and penguin.", main_test.get_user_input_twice())

if __name__ == '__main__':
    unittest.main()
