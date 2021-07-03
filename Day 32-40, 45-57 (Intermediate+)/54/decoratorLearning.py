# Functions -> inputs/functionality/output

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

# First Class objects: can be passed around as arguments (int, string, float)

def calculate(func, n1, n2):
    return func(n1,n2)

# Nested Function
def outer():
    print("I'm outer")
    def inner():
        print("I'm inner")
    return inner

# Return functions from other functions
inner_function = outer()
inner_function()

# Python Decorator

def decorate(a_function):
    def wrap():
        a_function()
    return wrap

import time

def delay_decorator(function):
    def wrap():
        time.sleep(2)
        function()
    return wrap

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_greeting():
    print("Greetings")

def say_bye():
    print("Goodbye")

say_hello()
say_bye()