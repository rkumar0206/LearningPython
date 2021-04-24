# Tuples
# Tuples are used to store multiple values in a single variable
# Features : Ordered , Unchangeable, Allow duplicates
# Tuples are written with round brackets

tuple1 = ("rohit", "mohit", "sagar", "nidhi", 12, 45, 56, True, False)
print(tuple1)

# printing length
print("Size of the tuple : " + str(len(tuple1)))

# Create tuple with one item
tupleWithOneItem = ("apple",)  # do not forget to add comma(,) at the end
print(tupleWithOneItem)

# tuple() constructor
newTuple = tuple(("a1", "a2", "a3"))
print(newTuple)

newTuple = tuple(tuple1)
print(newTuple)

print("------------------------------ Access Tuple -------------------------")

# By index number
print("item at index 0 : of tuple  " + str(tuple1) + " is " + str(tuple1[0]))

# By Negative indexing
print("item at index -1 : of tuple  " + str(tuple1) + " is " + str(tuple1[-1]))

# Range of indexes
print("item from index [1:4]  of tuple : " + str(tuple1) + " is " + str(tuple1[1:4]))

print("item from index [:4]  of tuple : " + str(tuple1) + " is " + str(tuple1[:4]))

print("item from index [2:]  of tuple : " + str(tuple1) + " is " + str(tuple1[2:]))

# Range of negative indexing
print("item from index [-3:-1]  of tuple : " + str(tuple1) + " is " + str(tuple1[-3:-1]))

print("-------------------------------------------------------------------")

print("--------------- Checking if item exists -------------------------------")

if "rohit" in tuple1:
    print("Yes, rohit is in tuple1")

print("-----------------------------------------------------------------------")

# Updating tuple item
# Tuples are unchangeable, but we can update the item by first converting tuple to list and convert list back to tuple
print("---------------------- Updating tuple items --------------------")

fruitsTuple = ("apple", "mango", "banana")
print("fruitsTuple : " + str(fruitsTuple))

print("Converting fruitsTuple to list")
fruitsList = list(fruitsTuple)
print("fruitsList : " + str(fruitsList))

print("Updating the item at index 1 to kiwi")
fruitsList[1] = "kiwi"

fruitsTuple = tuple(fruitsList)
print("fruitsTuple Updated : " + str(fruitsTuple))

# Using this method of converting tuple to list we can update,add, delete, etc in tuple

print("-----------------------------------------------------------------------")

print("---------------------------- Unpacking the tuple ---------------------------------")

# Unpacking the tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

# asterix (*) are used for assign rest of the values as list
(strings, *numbers, boolean1, boolean2) = tuple1

print("Strings : " + str(strings))
print("numbers : " + str(numbers))
print("boolean1 : " + str(boolean1))
print("boolean2 : " + str(boolean2))

print('-------------------------------------------------------------------------------')

# Looping tuple is similar to lists

# Joining tuple

print("------------------------- Joining tuple --------------------------------------")

tuple2 = (1, 5, 6, 8)
tuple3 = tuple1 + tuple2

print("Joining tuple1 and tuple2 to create new tuple3 : " + str(tuple3))

# Multiplying tuple
# Multiplying each item with 2 in tuple 1
tuple3 = tuple1 * 2
print("Multiplying each item of tuple with 2 : " + str(tuple3))

print('---------------------------------------------------------------------------------')
