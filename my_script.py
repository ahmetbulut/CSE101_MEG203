import math
from arithmetic import addition_of_two_numbers


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

# print("Hello World!")

# KISS: Keep It Simple Stupid!
# Add your comments

"""
This is a multi line comment
Thank you!
"""

pi = 3.1415926535897932 # I want to refer to the value of pi easily elsewhere.
my_variable = pi ** 2
# print(my_variable)

# result = type(42)
# print(result)
#

sqrt_of_16 = math.sqrt(16)

#
# print(math.sqrt(25))
# print(math.sqrt(100))
# print(math.sqrt(255))
#
# print("The result of the computation", sqrt_of_16)

the_result = addition_of_two_numbers(4, 5)

print(the_result)

# print_lyrics()
# print("Back to right after the call")



