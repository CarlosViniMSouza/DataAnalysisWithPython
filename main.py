# let's do all the intro to Python programming in the main.py file (when we start using Numpy, we'll go back to main.ipynb):

# Store input data in variables (moment 18:19)
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
