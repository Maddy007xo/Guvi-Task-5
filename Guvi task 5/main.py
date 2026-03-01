# Question - 1

# Creating a dictionary
people = [
    {"name": "Madhesh", "age": 15},
    {"name": "Vijay", "age": 22},
    {"name": "Sai", "age": 17},
    {"name": "Jaya", "age": 25}
]

#to filter people whose age is 18 or above
adult_over18 = list(filter(lambda person: person["age"] >= 18, people))

# to get only names for filtered list
names_adult_over18 = list(map(lambda person: person["name"], adult_over18))

# Printing the results
print("People age 18 or above:", adult_over18)
print("Names of adults:", names_adult_over18)

# Question - 2
# importing reduce function from functiontools

from functools import reduce

# creating a numbers list
numbers = [2,3,4,5,10,8,7,6]

# Using reduce and lambda functions to calculate product
product = reduce(lambda x, y: x * y, numbers)

# Printing the result
print("Product of all numbers:", product)

# Question - 3

# creating a numbers list
numbers = [10,222,355,444,50,66,77,88]

# Lambda function to check even number
even_numbers = lambda x: x % 2 == 0

# List comprehension to create squares of even numbers
squares = [num**2 for num in numbers if even_numbers(num)]

# Printing the results
print("Squares of the even numbers:", squares)

# Question - 4

# Creating Lambda function to check if a string is a number

number_check = lambda x: x.isdigit()

# Getting input from the user
User_input = input("Enter a string: ")

# Checking the given input and printing result
if number_check(User_input):
    print("The given string is a number.")
else:
    print("The given string is NOT a number.")

#Question - 5
# import datetime module

from datetime import datetime

# Creating a datetime object
current_date = datetime(2026, 2, 27)

# Creating Lambda function to extract year, month, day
get_date_parts = lambda d: (d.year, d.month, d.day)

# Call lambda function
year, month, day = get_date_parts(current_date)

# Printing the result
print("Year:", year)
print("Month:", month)
print("Day:", day)

