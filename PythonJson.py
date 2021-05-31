import json

# ------------------------ Parsing json ---------------------------------
# some json
temp_json = '{ "name": "Rohit", "age": 24}'

# parse temp_json using loads method json
parsed_json = json.loads(temp_json)

# the result is the python dictionary
print(parsed_json["age"])

# list json

list_json = '{"cars": [{"model": "BMW","mpg": 27.5},{ "model": "Maruti","mpg": 24.1}]}'

parsed_json = json.loads(list_json)

print(parsed_json)

# ---------------------------------------------------------------------------


# ------------------- Converting python objects json -----------------

# Converting from python dictionary to json

# a python dictionary object
x = {
    "name": "Mohit",
    "age": 22,
    "salary": 200000,
    "isMarried": False
}

# converting to json
converted_json = json.dumps(x)

print("Converted json : " + str(converted_json))

# We can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Object - dict, list, tuple,custom

# a list object
temp_list = ["Rohit", "Mohit", ["Arivind", "Sushila"], "Sagar"]
converted_json = json.dumps(temp_list)
print("Converted json (list) : " + str(converted_json))

# Examples
print(json.dumps({"name": "John", "age": 30}))  # dictionary
print(json.dumps(["apple", "bananas"]))  # list
print(json.dumps(("apple", "bananas")))  # tuple
print(json.dumps("hello"))  # string
print(json.dumps(42))  # int
print(json.dumps(31.76))  # float
print(json.dumps(True))  # Boolean true
print(json.dumps(False))  # Boolean false
print(json.dumps(None))  # none

# Using many data types in one object

temp_object = {
    "name": "Johny",
    "age": 45,
    "isMarried": True,
    "isDivorced": False,
    "children": ("Ann", "johny junior"),
    "pets": None,
    "cars": [
        {"model": "BMW", "mpg": 27.5},
        {"model": "Maruti", "mpg": 24.1}
    ]
}

converted_json = json.dumps(temp_object)
print("Converted json (custom object) without formatting: " + str(converted_json))

# formatting json using indent
converted_json = json.dumps(temp_object, indent=4)
print("Converted json (custom object) with formatting: " + str(converted_json))

# Order results
converted_json = json.dumps(temp_object, indent=4, sort_keys=True)
print("Converted json (custom object) with formatting and sorting: " + str(converted_json))
