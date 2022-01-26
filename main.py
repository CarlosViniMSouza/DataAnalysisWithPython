# let's do all the intro to Python programming in the main.py file (when we start using Numpy, we'll go back to main.ipynb):

# Store input data in variables (moment 18:19)
from numpy import empty

cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Perform the required calculations:
profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = number_of_bags * profit_per_bag

# Display the result:
print("the grocery store makes a total profit of $", total_profit)
# Output: the grocery store makes a total profit of $ 125.0

# Lets test the equity between variables

my_fav_num = 8
my_least_fav_num = 5
a_neutral_num = 1

print(my_fav_num == 8)
# Output: True

print(my_fav_num == my_least_fav_num)
# Output: False

print(my_fav_num != a_neutral_num)
# Output: True

print(my_fav_num != 8)
# Output: False

print(my_least_fav_num > a_neutral_num)
# Output: True

# Just like arithmetic operations, the result of a comparison operation can also stored in a variable

cost_of_ice_bag = 2.25
is_ice_bag_expen = cost_of_ice_bag >= 5
print("Is the ice bag expensive? \nAns: ", is_ice_bag_expen)

"""
String in Python have many built-in methods that can be used to manipulate them.
Lets try out some common string methods.

    Methods: Methods are functions associated with data types, and are
    accessed using the . notation e.g. variable_name.method() or "a string"
    .method() - Methods are a powerful technique for associating common operations with values of specific data types.

The .lower(), .upper() and .capitalize() methods are used to change the case of the characters.
"""

today = "Tuesday"

print(today.lower())
# Output: tuesday

print(today.upper())
# Output: TUESDAY

print(today.capitalize())
# Output: Tuesday

"""
LIST

A list in Python is an ordered collection of values. Lists can hold values of different data types, and support operations to add, remove and change values. Lists have the type list.

To create a list, enclose a list of values within square brackets '[' and ']', separated by commas.
"""

fruits = ['apple', 'banana', 'berries', 'strawberries']
print(fruits)
print(type(fruits))

# Creating a list of different data types:
stack = ['HTML + CSS + JS + YARN', 'Django', 'Django Rest', 'SQLite', 'Heroku']

a_list = [21, 'Carlos Souza', None, 1.79, stack, True]

print("The width of a_list is: ", len(a_list))

# Creating a empty list:

empty_list = []

"""
Tuples

A tuple isan ordered collection of values, similar to a list, however it's not possible to add, remove or modify values. A tuple is basically a immutable list.

Lets try some experiments with tuples:
"""

stack_tuple = ('HTML + CSS + JS + YARN', 'Django',
               'Django Rest', 'SQLite', 'Heroku')

print("The width of stack_tuple is:", len(stack_tuple))
# Output: The width of a_list is: 5

print(stack_tuple[1])
# Output: Django

print(stack_tuple[-2])
# Output: SQLite

"""
Dictionary:

A dictionary is an unordered collection of items Each item stored in a dictionary has a key and value. Keys are used to retrieve values from the dictionary. Dictionaries have the type dict.

Dictionaries are created by enclosing key-value pairs within curly brackets '{' and '}'
"""

my_login = {
    'name': 'Carlos Souza',
    'age': 21,
    'sex': 'Male',
    'married': False,
    'higth': 1.78
}

# This is a way for create a dictionary. See this second form:

my_login_num2 = dict(name='CarlosViniMSouza', age=20,
                     sex='Male', married=True, higth=1.81)

print(my_login)
# Output: {'name': 'Carlos Souza', 'age': 21, 'sex': 'Male', 'married': False, 'higth': 1.78}

print(my_login_num2)
# Output: {'name': 'CarlosViniMSouza', 'age': 20, 'sex': 'Male', 'married': True, 'higth': 1.81}

print(type(my_login))
# Output: <class 'dict'>

print("The width of dict is:", len(my_login_num2))
# Output: The width of dict is: 5

print(my_login_num2['name'])
# Output: CarlosViniMSouza

"""
The 'if' statement:

In Python, branching is done using the if statement, which is written as follows:

    if <condition>:
        <statement1>
        <statement2>

The condition can either be a variable or a expression. If the condition evaluates to True, then the 
statements within the if block are executed.
"""

mean = 8.5

if mean >= 6.0:
    print("Congratulations! You passed!")
else:
    print("Sorry, you reproved! :(")

# I added the 'else' to keep the code coherence.

# The session 'loops while()' and 'functions and sub-sessions' is very long.

"""
Modules and library functions:

We can already see that the EMI for Option 1 is lower than the EMI for Option 2. However, it would be nice to round up the amount to full dollars, rather than showing digits after the decimal.

However, since rounding numbers is a fairly common operation, Python provides a function for it (along with thousands of other functions) as part of the Python Standard Library.
Functions are organized into modules that need to be imported to use the functions they contain.

Modules: Modules are files containing Python code (variables, functions, classes, etc.). They provide a way of organizing the code for large Python projects into files and folders.
The key benefit of using modules is namespaces: you must import the module to use its functions within a Python script or notebook. Namespaces provide encapsulation and avoid naming 
conflicts between your code and a module or across modules.
"""

import math

print(help(math.ceil))
"""
Output:

ceil(x, /)
    Return the ceiling of x as an Integral.
    
    This is the smallest integer >= x.
"""

print(math.ceil(1.05))
# Output: 2
