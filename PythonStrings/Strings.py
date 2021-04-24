# assigning string variable

s = 'message'

# or

st = "Some message"
print(st)

# Multiline String

a = """\nHello sir my name is rohit kumar Singh, 
I am from Ranchi.
Currently I am doing my graduation from the Dr. Shyama Prasad Mukherjee College, Ranchi"""

print(a)

# OR

a = '''\nHello sir my name is rohit kumar Singh, 
I am from Ranchi.
Currently I am doing my graduation from the Dr. Shyama Prasad Mukherjee College, Ranchi'''

print(a)

# String as arrays

b = a[22]
print(b)

# LENGTH OF THE STRING

length = len(a)
print("Length of the string " + str(length))

# Checking for a particular word in the string

print("Rohit".lower() in a.lower())

# Checking for a particular word not in the string

print("rohit" not in a)

