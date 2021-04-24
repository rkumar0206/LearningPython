# In Python a function is defined using the def keyword:
def my_function():
    print("This is a test function.")


# Arguments
def print_my_name(name):
    print("Your name is " + str(name))


def print_my_full_name(fname, sname):
    print(fname + ' ' + sname)


# Arbitrary arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def print_all_names(*names):
    i = 0
    for x in names:
        print("name at index " + str(i) + "----" + str(x))
        i += 1


# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def key_args(child1, child2, child3):
    print("child 1 : " + str(child1))
    print("child 2 : " + str(child2))
    print("child 3 : " + str(child3))


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def kwargs(**children):
    print("child 1 -> " + str(children["child1"]))
    print("child 2 -> " + str(children["child2"]))
    print("child 3 -> " + str(children["child3"]))
    print("child 4 -> " + str(children["child4"]))


# Default parameter value

def print_any_name(name="rohit kumar singh"):
    print("Name is : " + str(name))


# Passing list as an argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def print_all_names_list(fruits):
    for f in fruits:
        print(f)


# Return Values
def sum_numbers(*numbers):
    return sum(numbers)


# Pass statement
# function definitions cannot be empty,
# but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def empty_func():
    pass


# Recursion
def recursion(x):
    if x > 0:
        result = x + recursion(x - 1)
        print(result)
    else:
        result = 0
    return result


# Calling  functions
my_function()
print_my_name("Rohit")
print_my_full_name("Rohit", "Kumar")
print_all_names("rohit", "mohit", "nidhi", "sagar")
key_args(child3="rohit", child2="mohit", child1="sagar")
kwargs(child1="rohit", child3="mohit", child2="sagar", child4="nidhi", child5="suraj")
print_any_name()
print_all_names_list(["apple", "mango", "orange"])
print("Sum of the numbers : " + str(sum_numbers(10, 10, 10)))
empty_func()
recursion(10)
