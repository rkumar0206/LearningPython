# The format() method allows you to format selected parts of a string.

# Adding placeholders
price = 49
txt = "The price of this item is {} dollars."
print(txt.format(price))

# Adding parameters inside the curly brackets to specify how to convert the value
price = 50.66678432
txt = "The price of this item is {:.2f} dollars."
print(txt.format(price))

# Multiple values
# if we want to use multiple values, add more placeholders and more values in format() method
quantity = 3
itemNo = 235
price = 1234.563
myOrder = "I want {} items of item number : {} for {:.2f} dollars in total.".format(quantity, itemNo,
                                                                                    (price * quantity))
print(myOrder)

# Index number
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

myOrder = "I want {0} items of item number : {1} for {2:.2f} dollars in total.".format(quantity, itemNo,
                                                                                       (price * quantity))
print(myOrder)

# if we want to refer to same value more than once use the same index number
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

txt = "I have a {carname}, it is a {model}."
print(txt.format(carname="Maruti", model="VXI"))
