# Dictionary : Dictionaries are used to store data values in key:value pairs.
# Features : Ordered, changeable, and does not allow duplicates

myDictionary = {
    "name": "Rohit",
    "age": 24,
    "isBoy": True,
    "hobby": ["music", "coding", "playing"]
}

print("myDictionary : " + str(myDictionary))

# Length of the dictionary
print("Length of the dictionary : " + str(len(myDictionary)))

# Accessing items
print("=================== Accessing Items =========================")

# We can access the dictionary by using key value
x = myDictionary["name"]
print("getting name from the myDictionary using myDictionary[\"name\"] : " + str(x))

# Using get() method
x = myDictionary.get("name")
print("getting name from the myDictionary using get() method : " + str(x))

# Getting the list of keys
keys = myDictionary.keys()
print("Keys of myDictionary using .keys() method : " + str(keys))

# Getting the list of values of the dictionary
values = myDictionary.values()
print("Values of the myDictionary using .values() method : " + str(values))

# Getting items using items() method : The items() method will return each item in a dictionary, as tuples in a list.
items = myDictionary.items()
print("Using the items() method to get the the items of myDictionary :  " + str(items))

# Checking if the key is there in the dictionary
if "age" in myDictionary:
    print("Yes, age is one of the key in the in the myDictionary dictionary")

print('------------------------------------------------------------------------')

# Changing the items
print("=================== Changing Items =========================")

# we can change the items value by referring to its key
myDictionary["name"] = "Mohit kumar"
print("Changing the value of name in myDictionary  : " + str(myDictionary))

# Using update method to change the value
myDictionary.update({"age": 25})
print("Changing/Updating  the age value using the update() method : " + str(myDictionary))

print('------------------------------------------------------------------------')

# Adding items
print("=================== Adding Items =========================")

# Adding method by using below method
myDictionary["isMarried"] = False
print("Adding a new item (isMarried) to the myDictionary : " + str(myDictionary))

# Using update() method
myDictionary.update({"company": "TCS"})
print("Adding new item (company) to the myDictionary using update() method :  " + str(myDictionary))

print('------------------------------------------------------------------------')

# Removing items
print("=================== Removing Items =========================")

# Using pop() method ny referring to the key
myDictionary.pop("company")
print("Removing the item (company) from the myDictionary using pop() method : " + str(myDictionary))

# Using popItem() method : The popitem() method removes the last inserted item
myDictionary.popitem()
print("Removing the last inserted item in myDictionary using popItem() method :  " + str(myDictionary))

# Using del keyword vy referring to the key
myDictionary["isMarried"] = False
del myDictionary["isMarried"]
print("Using del keyword for removing the isMarried item from the dictionary : " + str(myDictionary))

# Using del keyword for deleting the  dictionary
dict1 = {
    "item1": "item_name",
    "item2": "item_info"
}

print("dic1 : " + str(dict1))
del dict1
print("Deleting the dic1 dictionary using del keyword")

# Using clear() method for emptying the dictionary
tempDict = {
    "item1": "item_name",
    "item2": "item_info"
}

print("tempDic = " + str(tempDict))
tempDict.clear()
print("Clearing the tempDic dictionary using clear() method : " + str(tempDict))

print('------------------------------------------------------------------------')

# Looping
print("=================== Looping dictionary =========================")

# Looping on values
print("Looping on values : ")
for x in myDictionary.values():
    print(x)

# Looping on keys
print("Looping on keys : ")
for k in myDictionary.keys():
    print(k)

# Loop through both keys and values, by using the items() method
print("Loop through both keys and values, by using the items() method:")
for k, v in myDictionary.items():
    print("Key : " + str(k) + " and value : " + str(v))

print('------------------------------------------------------------------------')

# Copying dictionary
print("=================== Copy dictionary =========================")

# using copy() method
tempDict = myDictionary.copy()
print("Copying the myDictionary to tempDict using copy() method : " + str(tempDict))

# using the dict() constructor method
dict1 = dict(tempDict)
print("Copying the tempDict to tempDict using dict() method : " + str(dict1))

print('------------------------------------------------------------------------')

# Nested Dictionaries
print("=================== Nested dictionary =========================")

myFamily = {
    "child1": {
        "name": "Rohit",
        "age": 24
    },

    "child2": {
        "name": "Mohit",
        "age": 22
    },

    "child3": {
        "name": "Sagar",
        "age": 13
    }
}

print("Nested dictionary : " + str(myFamily))

# or we can add like this

child4 = {
    "name": "Nidhi",
    "age": 15
}
child5 = {
    "name": "Arvind Kumar Singh",
    "age": 47
}

myFamily = {
    "child4": child4,
    "child5": child5
}
print(myFamily)

print('------------------------------------------------------------------------')
