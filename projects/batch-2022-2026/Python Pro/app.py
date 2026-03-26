# name = "afnan" #string
# phone = "5334" #integer
# marks = 90.5 #float
# print(name)
# print(phone)


# # Write a student database which has name, phone number, age, department, college.
# # Example of Immutable
# x = 10
# y = x
# y = 20
# print(y)

# # Example of Mutable
# Fruits = ["apple", "banana", "cherry"]
# print(Fruits)

# #Adding to list
# Py_b5 = ["AKash", "Rida", "Khizar"]
# Py_b5.append("Afnan")
# print(Py_b5)
# Extend
# numbers = [1, 2, 3]
# numbers.extend([4, 5, 6])
# print(numbers)

# #Removing from list
# Py_b5.remove("Rida")
# print(Py_b5)

# #Input statements

# name =input("Enter your name: ")
# print(name)
# phone =input("Enter your phone number: ")
# age =input("Enter your age: ")

# print(phone)
# print(age)

# Take input values from a student & of their 
# subject marks of 4 subjects & print write after the questions

# WRITE A LIST OF FAV PHONE COMPANY ANY 3 & THEN ADD NOKIA AS A 4TH COMPANY AND PRINT THE LIS




# Data Types in Python
# strings
#integer
#float
#boolean - True/False

# Write a program to store the following details:
# name
# Marks
# Roll Number   


# Creating a list of numbers
# a = [1, 2, 3]  # List containing integers

# Creating a list of fruits
# b = ["apple", "banana", "mango"]  # List containing fruit names

# Remove the last element from the list using pop()
# b.pop(-1)  # pop(-1) removes the element at the last index

# Print the modified list after removal
# print(b)  # Output: ['apple', 'banana']

# Sum in list
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))



#Cretate a list of 10 students & then add 3 students
# more to the list & then remove the first & last 2nd student name from
#the list & then add a student name after the 3rd student
# name & print all the statements one by one.

# List Slicing
# nums = [10, 20, 30, 40, 50, 60]
# print(nums[2:4])
#Modify the list
# nums[4] = 70
# print(nums)


# write a program to a list of 15 students & then print the first 5 students, 
# then print the 6 to 8 students name

# Create a list of numbers
# nums = [10, 20, 30, 40, 50, 60]
# Add an element at the end of the list
# nums.append(20)
# Print the list after append
# print(nums)

# Insert an element at index 2
# nums.insert(2, 90)
# Print the list after insert
# print(nums)

# Modify the element at index 4
# nums[4] = 70

# Extend the list by adding multiple elements
# nums.extend([80, 90, 100, 101])

#remove an element from the list
# roll = [10, 20, 30, 40, 50, 60]
# roll.remove(30)
# print(roll)
#roll.pop(-1)
# print(roll)
# roll.clear()
# print(roll)

#range
# for i in range(0, 21, 2):
#     print(i)
    
# range (start, stop, step)
# for i in range(11, 0, -3):
#    print(i)

# string in range
# students = ["apple", "banana", "cherry", "date", "elderberry"]
# for i in range(0, 4):
#    print(students[i])

# print the length of the list
# fruits = ["apple", "org", "banana", "mango", "grape", "orange", "kiwi", "watermelon", "peach", "pear", "plum"]
# print(len(fruits))

# write a program having a list of 8 students name & then printing each students
# name along side the index number of the student in the list. (use range function)

# converting range () to list
#numbers = list(range(1, 11)) # range() itself does not produce a list
# print(numbers)                  # It produce a range object, so we convert it to a list using list() function

# Advantages of range() / Practical applications
# Printing tables
# counting
# indexing lists
# loops
# automation

# important Note
# Stop values are not included in the range, so if you want to print numbers 
# from 1 to 10, you need to use range(1, 11) because 11 is not included in the output.
# Default start is 0
# Default step is 1
# steps can be negative


# Example -1: Print N0. 1 to 10
# Example -2: Print Even Nos. from 1 to 20
# Example -3: Sum of Numbers (using range)

# Loops in Python

# Two types of loops in Python
# 1. For Loop
# 2. While Loop

#Example-1 For Loop
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in fruits:
    print(i)
    
# Example -2 While Loop
i = 1
while i <=10:
    print(i)
    i += 2

# Infinite loop
i=1
while i<=5:
    print(i)
    
i = 1
while i <=10:
    print(i)
    i += 2