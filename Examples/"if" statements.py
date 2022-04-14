# Variables used in the example ``if`` statements
"""a = 4
b = 5

# Basic comparisons
if a < b:
    print("a is less than b")

if a > b:
    print("a is greater than b")

print("Done")"""

'''a = 5
b = 6

#>= <= must be in order like so
if a <= b:
    print("a is less than or equal to b")

if a >= b:
    print("a is greater than or equal to b")

# Equal
if a == b:
    print("a is equal to b")

# Not equal
if a != b:
    print("a and b are not equal")'''

""""# This is wrong
a == 1

# This is also wrong
if a = 1:
    print("A is one")"""

'''a = 6
b = 6
c = 8

# And
if a < b and a < c:
    print("a is less than b and c")

# Non-exclusive or
if a < b or a < c:
    print("a is less than either b or c (or both)")'''

# Boolean data type. This is legal!
'''a = False

if a:
    print("a is true")

# How to use the not function
if not a:
    print("a is false")'''

'''a = True
b = False

if a and b:
    print("a and b are both true")'''

'''a = 3
b = 3

# This next line is strange-looking, but legal.
# c will be true or false, depending if
# a and b are equal.
c = a == b

# Prints value of c, in this case True
print(c)'''

'''if 1:
    print("1")
if "A":
    print("A")'''

'''temperature = input("What is the temperature in Fahrenheit? ")
print("You said the temperature was " + temperature + ".")'''

''''#Get temp from user
temperature = int(input("What is the temperature in Fahrenheit? "))

#convert the input to an integer
temperature = int(temperature)

#Do our comparison
if temperature > 90:
    print("It is hot outside.")'''

#Get temp from user
#chain input and int function like this:
temperature = int(input("What is the temperature in Fahrenheit? "))

#The program reads in order so make sure to keep it great to least. If not it will skip the greater condition
#if below lesser values
if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")

elif temperature > 90:
    print("It is hot outside.")

#chain elif = "if" and "else"
elif temperature < 30:
    print("It is cold outside.")

else:
    print("It is not hot outside.")
print("Done")

''''#Case sensative comparison
user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")

user_name = input("What is your name? ")
if user_name == Paul: # This does not work because quotes are missing
    print("You have a nice name.")
else:
    print("Your name is ok.")'''


''''# This does not work! It will always be true
if user_name == "Paul" or "Mary":

# This does work
if user_name == "Paul" or user_name == "Mary":'''

''''#Case-insensitive text use command .lower()
user_name = input("What is your name? ")
if user_name.lower() == "paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")'''