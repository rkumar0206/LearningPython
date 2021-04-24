import datetime

# Printing current date and time
date = datetime.datetime.now()
print(date)

print("Year {}".format(date.year))
# Formatting date and time using strftime() method
# Reference to all the valid date format : https://www.w3schools.com/python/python_datetime.asp

print("WeekDay {}".format(date.strftime("%A")))
print("Month {}".format(date.strftime("%B")))
print("Year {}".format(date.strftime("%C")))

# Creating date object
date = datetime.datetime(2020, 6, 2)
print(date)
print(date.strftime("%A"))
