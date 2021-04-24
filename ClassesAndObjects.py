class FirstClass:
    a = 5


# The __init__() function is called automatically every time the class is being used to create a new object.

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastname = lname


# Class with functions other than __inti__
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def printEmployeeDetails(self):
        print(
            "Employee name : " + self.name + "\n" + "Employee salary : " + str(
                self.salary) + "\n" + "Employee age : " + str(self.age))


# Using the classes
print(FirstClass.a)
print()
p1 = Person("Rohit", "Kumar Singh")
print("Person name " + p1.firstName + ' ' + p1.lastname)
print()
e1 = Employee("Rohit", 24, 200000)
e1.printEmployeeDetails()
print()
e2 = Employee("Mohit", 22, 400000)
e2.printEmployeeDetails()
print()

# Modifying the e2 value
print("Modifying the e2.salary value of the class Employee ")
e2.salary = 4100000
e2.printEmployeeDetails()

# Deleting the e2 object

del e2
# e2.printEmployeeDetails() will raise an error
