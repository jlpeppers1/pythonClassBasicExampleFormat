#Below assumes we are using unit tests

#Generally put your doc string at the Top.
#When you have modified and filled out the below doc string
#delete this line and the 2 lines above it
"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

This program tests a function that prints 'Hello World'
as output.  The function is then called.
"""

#general structure of each unit test should be:
#docstring
#imports
#global variables
#classes and functions
#driver code or main code; the 'if __name__ == '__main__' section

#Delete above; but for more examples

#When done, delete from here ----------------------
#Imports section
    #all if your imports should go here
    #here are some examples:
import unittest
#if we are mocking user typed in input
import unittest.mock as mock
#import file to test
from mainFolder import main_class_example as main_test
#-------------------------------------------to here

#When done, delete from here ----------------------
#Global variables section section
    #if not importing them, put global variables here
    #here are some examples:
PI = 3.14159265358979323
#-------------------------------------------to here

#When done, delete from here ----------------------
#classes and functions section
    #if not importing them, put functions here
#for unit testing generally start with:
class MyTestCase(unittest.TestCase):

    #notice all tests must start with test_* for the name
    def test_basic(self):
        #commonly can use:
            #assertTrue(), assertEqual(), assertFalse(), assertRaises()
        #basic function call
        self.assertEqual(main_test.hello_world(), None)
        #above equals none because hello world just prints; doens't return

    #another test; still test_* for the name
    def test_call_with_value(self):
        self.assertEqual(main_test.PI, main_test.get_pi(True))

    def test_one_input_mock(self):
        #notice this line
        with mock.patch('builtins.input', return_value="turtle"):
            self.assertEqual("turtle", main_test.get_user_input_once())

    def test_multiple_input_mock(self):
        #notice this line
        with mock.patch('builtins.input', side_effect=["turtle", "penguin"]):
            self.assertEqual("You input turtle and penguin.", main_test.get_user_input_twice())
#-------------------------------------------to here

#When done, delete from here ----------------------
#driver code, or 'main' code
    #this code only runs when you run this specific file
    #you can call your defined functions or classes here
    #here is an example
#always have this; usually don't change for unit tests
if __name__ == '__main__':
    unittest.main()
#-------------------------------------------to here
