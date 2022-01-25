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

print(len("The width of stack_tuple is:", stack_tuple))
# Output: The width of a_list is: 5

print(stack_tuple[1])
# Output: Django

print(stack_tuple[-2])
# Output: SQLite
