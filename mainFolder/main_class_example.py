#Generally put your doc string at the Top.
#When you have modified and filled out the below doc string
#delete this line and the 2 lines above it
"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

Change this description to be more relevant.
This program creates a function that prints 'Hello World'
as output.  The function is then called.
"""

#general structure of each file should be:
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
#import random
#from folder_path import python_file_name
#from folder_path import_python_file_name as easier_to_use_variable
#-------------------------------------------to here

#When done, delete from here ----------------------
#Global variables section section
    #if not importing them, put global variables here
    #here are some examples:
PI = 3.14159265358979323
#-------------------------------------------to here

#When done, delete from here ----------------------
#classes and functions section
    #if not importing them, put functions
    #here are some examples:
def hello_world():
    print('hello world!')
#another function, returns a value, takes an input of true or false
def get_pi(x):
    if (x):
        return PI
    else:
        return 0

def get_user_input_once():
    user_input = input("please enter a value")
    return user_input

def get_user_input_twice():
    user_input_one = input("please enter a value")
    user_input_two = input("please enter a different value")
    return_string = "You input " + user_input_one + " and " + user_input_two + "."
    return return_string
#-------------------------------------------to here

#When done, delete from here ----------------------
#driver code, or 'main' code
    #this code only runs when you run this specific file
    #you can call your defined functions or classes here
    #here is an example
#always have this
if __name__ == '__main__':
    #call our functions
    hello_world()
    boolean_value_variable = True
    #store it as a variable since get_pi returns a value
    pi_value = get_pi(boolean_value_variable)
    #cast it as a string before printing!
    print("The value of pi is " + str(pi_value))
#-------------------------------------------to here
