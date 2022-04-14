"""
x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))

x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))
"""

#list
"""
x = [10, 20]
print(x)
"""

#single list
"""
print(x[0])
"""

#backside of an array
'''
x = [10, 20, 30]
print(x[-1])
'''

#Create an empty list
'''
my_list = []
'''

'''
my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)
'''

#string list
'''
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)
'''

#list in list
'''
my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)
'''

'''
my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])
'''

'''
for index, value in enumerate(my_list):
    print(index, value)
'''

#Adding new items to list
'''
my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)
'''

#Creating a list of numbers from user input
'''
# Create an empty list
my_list = []

for i in range(5):
    user_input = input( "Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)
'''

# Create an array with 100 zeros.
'''
my_list = [0] * 100
'''

#summing the values in a list V1
'''
# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[index]

# Print the result
print(list_total)
'''

#summing the values in a list v2
'''
# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop through array, copying each item in the array into
# the variable named item.
for item in my_list:
    # Add each item
    list_total += item

# Print the result
print(list_total)
'''

#Doubling all the numbers in a list
'''
# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Modify the element by doubling it
    my_list[index] = my_list[index] * 2

# Print the result
print(my_list)
'''


#Accessing a string of list
'''
x = "This is a sample string"
#x = "0123456789"

print("x=", x)

# Accessing the first character ("T")
print("x[0]=", x[0])

# Accessing the second character ("h")
print("x[1]=", x[1])

# Accessing from the right side ("g")
print("x[-1]=", x[-1])

# Access 0-5 ("This ")
print("x[:6]=", x[:6])
# Access 6 to the end ("is a sample string")
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])
'''

#adding and multiplying strings
'''
a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))
'''

#Getting the length of a string or list
'''
a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))
'''

d=['JAN','FEB','MAR','April','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
N = int(input("Enter a month number: "))
for i in range(len(d)):
    if d[i] == N:
        month=(i+1)
print(month)

n = int(input("Enter a month number: "))
