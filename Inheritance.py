# Inheritance allows us to define class that inherits all the methods and properties from another class
# ====================================================================
class Person:
    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age

    def printPersonDetails(self):
        print("Name : " + self.firstname + ' ' + self.lastname)
        print("Age : " + str(self.age))


# -------------------------------------------------------------------------------------

class Test(Person):
    pass


# ----------------------------Single inheritance --------------------------------------

# Using child class  __init__ method
class Teacher(Person):
    def __init__(self, first_name, last_name, age, salary):
        Person.__init__(self, first_name, last_name, age)  # Using parent class name
        self.salary = salary

    def printTeachersInfo(self):
        self.printPersonDetails()
        print("Salary : " + str(self.salary))


# ----------------------------Single inheritance --------------------------------------
class Student(Person):
    def __init__(self, first_name, last_name, age, roll_number, *subjects):
        super().__init__(first_name, last_name, age)  # using super() method , super() refer to the parent class
        self.subjects = subjects
        self.rollNo = roll_number

    def printStudentDetails(self):
        self.printPersonDetails()
        print("Student's roll number : " + str(self.rollNo))
        print("Subjects : " + str(self.subjects))
        print("Main subject : " + str(self.subjects[2]))


# -------------------------------------------------------------------------------------

# -------------------------- Multiple inheritance --------------------------------------

# Multiple inheritance
class Base1:
    def __init__(self):
        self.str1 = "Base1"
        print(self.str1)


class Base2:
    def __init__(self):
        self.str2 = "Base2"
        print(self.str2)


class Derived(Base1, Base2):
    def __init__(self):
        self.str3 = "Derived"
        print(self.str3)
        Base1.__init__(self)
        Base2.__init__(self)


# -------------------------------------------------------------------------------------

# ----------------------------Multi level inheritance ------------------------------

class Parent:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age


class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def getAddress(self):
        return self.address


# -------------------------------------------------------------------------------------

# Using class
t = Test("Rohit", "Kumar", 34)
t.printPersonDetails()
print()

teacher = Teacher("Tom", "", 20, 1000)
teacher.printTeachersInfo()
print()

student = Student("Sagar", "Singh", 13, 45, "english", "hindi", "maths", "science", "sst")
student.printStudentDetails()
print()

print("Demonstrating Multiple inheritance")
derived = Derived()  # making the derived class object
print()

print("Demonstrating Multilevel inheritance")
grandChild = GrandChild("Rohit", 24, "Vidyanagar")
print("Name = " + grandChild.getName())
print("Age = " + str(grandChild.getAge()))
print("Address = " + grandChild.getAddress())
