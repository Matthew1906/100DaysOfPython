# What we'll learn:

# 1. OUTPUT STRING IN CONSOLE
print("Hello, World!") # double quotes-> between the quotes are texts that the coder want to print
# -> a string of characters
# double quotes -> show the beginning and the end of the string

# when there is an ERROR -> COPY the ERROR MESSAGE, PASTE it on GOOGLE
# most of the time the solution is in STACK OVERFLOW

# you can switch around between double and single quotes
print("I'm extremely hungry")# single inside double
print('He said,"I wish that i could be like the cool kids!') #double inside single
# callback to 'Cool Kids' by Echosmith

# backslash n
print("Hello, it's me\nI was wondering if after all these years you'd like to meet") #use \n to create enter
# callback to 'Hello' by Adele

# concatenate literal strings
print("Hello!"+" My name is Matthew")

# INDENTATION IS VERY IMPORTANT

# DEBUGGING EXERCISE
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign')
print('e.g. print("Hello" + "world")')
print("New lines can be created with a backslash and n")

# 2. INPUT FUNCTIONS
input("What is your name?\n") # the inputted data is passed into the input
# the program paused until the user input something
# syntax = input(prompt) -> prompt = string

print("Hello "+ input("What is your name?\n")) # you can do this too
# input first-> then print hello + inputted string

# INPUT EXERCISE
print(len(input("What is your name? ")))
# len -> length of a string


# 3. VARIABLES
name = input("What's my name? ") # like taking notes into a notebook
# variables are useful so that we can refer back to the value

length = len(name)

# VARIABLE EXERCISE
a = input("a: ")
b = input('b: ')

c = a
a = b
b = c

print("a = "+a)
print("b = "+b)

# VARIABLES NAMING -> BASIC RULES AND BEST PRACTICES
# 1. MAKE SURE THE NAMES MAKE SENSE
# 2. YOU CAN'T ADD SPACES OR USE KEYWORDS
# 3. SEPARATE WORDS USING UNDERSCORE -> IN PYTHON -> BEST PRACTICE


