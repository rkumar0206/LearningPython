# Sets are used to store multiple items in one variable like lists
# Features : Unordered (No index number), No-Duplicates allowed,
# we cannot change the items in the sets once created but we can  add new items

# Creating set
mySet = {"one", "two", "three", 1, 2, 3, True, False}
print(mySet)

# Length of the set
print("Length of the set : " + str(len(mySet)))

# Set constructor
newSet = set(("Lion", "Tiger", "Wolf"))
print("Set created with set constructor : " + str(newSet))

# Access Items
print("-------------------------- Access Items -----------------------------")

# loop
for s in mySet:
    print(s, end=" ")

print()

# Checking if the item is in the set
if "one" in mySet:
    print("Yes, one is in mySet")

print("-------------------------------------------------------------------------")

# Adding items to the list
print("------------------------- Adding Items ------------------------------")

# add() method
mySet.add("Hundred")
print("Added an element  Hundred : " + str(mySet))

# Adding another set
set2 = {23, 56, 76}
mySet.update(set2)
print("Adding elements of another set : " + str(mySet))

# Adding any iterable

list1 = [98, 467, 754]
mySet.update(list1)
print("Adding elements of another list : " + str(mySet))

print("-------------------------------------------------------------------------")

# Removing elements from the set
print("------------------------- Removing Items ------------------------------")

# using remove() method
mySet.remove(98)  # Note : if the item to be removed is not present in the set then remove() will raise an error
print("Removing element 98 from the set using remove method : " + str(mySet))

# Using discard() method
mySet.discard(
    "one")  # Note : if the item to be removed is not present in the set then discard() will not raise any error
print("Removing element 'one' from the set using discard() method : " + str(mySet))

# Using pop() method
# Note : Sets are unordered therefore we don't know which item is being removed
mySet.pop()
print("Using pop() method : " + str(mySet))

# Using clear() method : it will empty the set
set2.clear()
print("Using clear() method on the set2 set : " + str(set2))

# Using del keyword to delete the set completely
del set2
print("Using del keyword on set set2")

print("-------------------------------------------------------------------------")

# Joining sets
print("------------------------- Joining sets ------------------------------")

# Using union() method
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print("set1 : " + str(set1))
print("set2: " + str(set2))
print("Joining set1 and set2 Using union() method : " + str(set3))

# intersection : Keep only the duplicate items in both the sets

# Using intersection_update() method will keep only the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

print("set1 : " + str(set1))
print("set2: " + str(set2))
set1.intersection_update(set2)
print("Using intersection_update() method on set1 to intersect set2: " + str(set1))

# Using intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("set1 : " + str(set1))
print("set2: " + str(set2))

set3 = set1.intersection(set2)
print("Using intersection() method on set1 and set2 to get set3 : " + str(set3))

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("set1 : " + str(set1))
print("set2: " + str(set2))

set1.symmetric_difference_update(set2)
print(
    "Using symmetric_difference_update() method for getting the elements which are not in both the sets : " + str(set1))

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("set1 : " + str(set1))
print("set2: " + str(set2))

set3 = set1.symmetric_difference(set2)
print(
    "Using symmetric_difference() method for getting the elements which are not in both the sets in another set set3 : " + str(
        set3))

print("-------------------------------------------------------------------------")

# methods related to sets

# Method	Description

# add()	- Adds an element to the set
# clear()	 - Removes all the elements from the set
# copy()	- Returns a copy of the set
# difference()	 - Returns a set containing the difference between two or more sets
# difference_update() - Removes the items in this set that are also included in another, specified set
# discard()	- Remove the specified item
# intersection()	- Returns a set, that is the intersection of two other sets
# intersection_update()	- Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	- Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset()	- Returns whether this set contains another set or not
# pop()	- Removes an element from the set
# remove()	- Removes the specified element
# symmetric_difference()	- Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	- inserts the symmetric differences from this set and another
# union()	- Return a set containing the union of sets
# update() - Update the set with the union of this set and others
