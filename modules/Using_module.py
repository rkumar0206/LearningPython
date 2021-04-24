# Importing the module
import simple_maths_module as smm  # renaming thr module name

a = 12
b = 34

s = smm.SimpleOperations(a, b)
print("Sum of {} and {} is : ".format(a, b) + str(s.sum()))
print("Difference of {} and {} is : ".format(a, b) + str(s.difference()))
print("Multiplication of {} and {} is : ".format(a, b) + str(s.multiply()))
print("Division of {} and {} is : {:.2f}".format(a, b, s.divide()))
print()

# importing built-in module
import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

# importing only specific item from module
from math import sin

x = sin(30)
print("Value of sin(30) : is {:.3f}".format(x))
