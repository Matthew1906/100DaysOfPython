# 1. FUNCTIONS WITH INPUT, PARAMETER, ARGUMENTS

# WITHOUT INPUTS
def greet():
    print("Hello")
    print("How are you?")
    print("Great! Bye")
greet()

def greetSomeone(name): #parameter = name of the data, argument = value of the data
    print("Hello "+name)
    print("How are you?")
    print("Great! Bye")
greetSomeone("Johnny")

# 2. POSITIONAL vs KEYWORD arguments

# positional argument -> position and sequence of arguments REALLY matter
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
greet_with("Mike", "London")

# keyword arguments -> specify the parameter's values when calling the function
greet_with(location = "Jakarta", name="Joko")
