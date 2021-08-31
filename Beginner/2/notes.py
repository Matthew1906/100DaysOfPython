# DATA TYPES, NUMBERS, OPERATIONS, TYPE CONVERSION, f-Strings

# 1. Data Types

# a. String
# pulling out an element from the string = subscripting
# the index starts from 0 to length-1

print("Hello"[3])

# b. Integer

# large integers can be separated with _
print(199_000) # show 199000, but it makes it more readable for us

# c. Float = floating point number

print(3.41231231)

# d. Boolean = True or False

print(True)

# 2. Type Error, Type Checking, Type Conversion

# Type Error -> when we give the wrong type to the function

print(type("aPPLE")) # CHECK THE TYPE OF THE VALUE/VARIABLE

# TYPE CASTING -> CONVERT INTO ANOTHER VALUE

num_str = str(100)
print("My Wishful Score is "+ num_str)

# DATA TYPE EXERCISE
two_digit_number = input("Type a two digit number: ")
if len(two_digit_number)!=2:
    print("Invalid input")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# 3. Mathematical Operators
# '-' Substraction
# '*' Multiplication
# '**' Exponent
# '/' Division -> float result
# '//' Division -> number result
# '%' Modulus
# Priorities -> (), **, * / , + -

# MATHEMATICAL OPERATOR EXERCISE -> BMI CALCULATOR
# Count Body Mass Index with formula = weight/(height^2)

weight = float(input("Input your Weight (kg): "))
height = float(input("Input your Height (m): "))
print("Your BMI index (simplified) is "+ str(int(weight/(height**2))))

# Number Manipulation and F Strings
print(round(10/3,2)) # round function -> how many decimal places
# shorthand => symbol + '='

# f-string

score = 86
print(f'Your score is {score}')

# MATHEMATICAL MANIPULATION EXERCISE -> LIFE IN WEEKS
# Count how many days, weeks, and months left if you live until 90 

age = int(input("What is your current age? "))
days = (90-age)*365
weeks = (90-age)*52
months = (90-age)*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")