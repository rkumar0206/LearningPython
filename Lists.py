myList = [1, 2, 3]
print(myList)

print("--------------------------------- Basics of list -------------------------------")
# LENGTH OF THE LIST
print("current length of the list : " + str(len(myList)))

# DUPLICATES ARE ALLOWED
myList.append(2)
print("Duplicates are allowed : " + str(myList))

# LIST CONSTRUCTOR
anotherList = list((2, 4, 5, 6))
print("Making list using constructor : " + str(anotherList))

print("------------------------------------------------------------")

print("---------------------------- ACCESS THE LIST ------------------------------")

print("Second element of the list : " + str(anotherList[1]))

# NEGATIVE INDEXING
print("Last element of the list : " + str(anotherList[-1]))
print("Second last element of the list : " + str(anotherList[-2]))

# RANGE OF THE INDEXES
print("Element 2 to 3 " + str(anotherList[1: 3]))  # prints first, second and third
print("Element from 1 to 3 :" + str(anotherList[:3]))

print("----------------------------------------------------------------------------")

print("---------------------------- CHANGE THE LIST ------------------------------")

# changing one item i.e. second item
myList[1] = 47
print("Replacing the second item with 47 : " + str(myList))

# replace the second and third value with 23 and 45

myList[1:3] = [23, 45]  # if we will insert more than you replace, the new item will be inserted where you specified,
# and remaining will move accordingly
print("replace the second and third value with 23 and 45 : " + str(myList))

# change the second value by replacing it with two new values

myList[1:2] = [100, 200]
print("change the second value by replacing it with two new values i.e 100 and 200 : " + str(myList))

# change the second and third value by replacing it with the one value
myList[1:3] = [400]
print("change the second and third value by replacing it with the one value i.e. 400 : " + str(myList))

print("----------------------------------------------------------------------------")

# --------------------------------- ADD TO LIST -------------------------------------

print("------------------------- Adding elements to list -----------------------------")

# Using append method
myList.append(25)
print("append method is used to insert value at the end of the list here 25: " + str(myList))

# Using the insert method
myList.insert(2, 56)
print("insert method is used to insert value at the specified index of the list here 2 - 56: " + str(myList))

# Using extend method : used for appending the elements of the another list, tuple, set, dictionaries
myList.extend(anotherList)
print("Using extend method : used for appending the elements of the another list : " + str(myList))

print("------------------------------------------------------------")

# Removing elements from the list

print("---------------------------- Remove elements from THE LIST ------------------------------")

# Using remove method - removes specified element

myList.remove(56)
print("Removing element 56 from the list : " + str(myList))

# Using the pop() method
# pop(index) method is used to remove element from the specified index
# pop() method without index number removes the last item

myList.pop()
print("using pop() to remove the last element from the list : " + str(myList))

myList.pop(3)
print("using pop(3) to remove the fourth element from the list : " + str(myList))

# clear method : this method empties the list
anotherList.clear()
print("Using myAnotherList.clear() for removing all the elements from the list : " + str(anotherList))

# del keyboard is also used for removing element at specified index or deleting the entire list

del myList[1]
print("Using del myList[1] for deleting the second element from the list : " + str(myList))

tempList = [23, 45, 67]
del tempList  # wil delete the entire list

print("----------------------------------------------------------------------------")

# Looping through list
print("Looping through the list")
for n in myList:
    print(n, end=', ')

print()

for i in range(len(myList)):
    print('index ' + str(i), end=', ')

print()

# List comprehension

fruits = ["apple", "mango", "litchi", "kiwi", "banana", "cherry"]
newList = [x for x in fruits if "a" in x]

print(newList)

newList = [x for x in myList]
print(newList)

newList = [x for x in range(10)]
print(newList)

newList = [x for x in range(10) if x < 5]
print(newList)

# set the elements of the newList to upper case
newList = [x.upper() for x in fruits]
print(newList)

# set the all the elements of the newList to "hello"
newList = ["hello" for x in fruits]
print(newList)

# return "orange" instead of banana
# The expression in this example says:
# "Return the item if it is not banana, if it is banana return orange".
newList = [x if x != "banana" else "orange" for x in fruits]
print(newList)

print("----------------------------------------------------------------------------------")

# Sorting list
print("--------------------- Sorting list -----------------------")

# Sort the list alphabetically or numerically
myList.sort()
print(myList)

fruits.sort()
print(fruits)

# Sort the list alphabetically or numerically in descending order
myList.sort(reverse=True)
print(myList)

fruits.sort(reverse=True)
print(fruits)

# Case Insensitive
# By default the sort method is case sensitive

fruits.append("Mango")
fruits.append("AAPPLLEE")
fruits.append("Cherry")
fruits.sort(key=str.upper)  # Case insensitive

print(fruits)

# Reversing the list
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

fruits.reverse()
print(fruits)

print("----------------------------------------------------------------------------------")

print('------------------------- Copying the list ------------------------')

# using copy method
newList = fruits.copy()
print(newList)

# Using list constructor
newList = list(myList)
print(newList)

print('----------------------------------------------------------------------')

print('------------------------- Joining the list ------------------------')

list1 = [1, 2, 34, 5, 6, 7, 9, 0, 0]
list2 = ["one", "two", "three", "four", "five"]

# using + operator
newList = list1 + list2
print(newList)

# Using extend() method

list1.extend(list2)
print(list1)

for x in list2:
    list1.remove(x)

# using loop
for x in list2 :
    list1.append(x)
print(list1)

print('----------------------------------------------------------------------')
