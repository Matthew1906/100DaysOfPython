# Advanced Python Arguments
# Create arguments with default values
# When defining function, set the value of the arguments -> become default
# we can change it's value using keyword inputs
#  = -> there is a default
# we only need to provide the required arguments

#  *args = Many positional arguments

# Unlimited Arguments, example = add any number of arguments
# add *args in the parameter

def add(*numbers):
    result = 0
    for number in numbers:
        result+=number
    return result

print(add(1,2,3,4,5,6,7,8,9,10))

# **kwargs limitless keyword arguments

def calculate(number,**kwargs):
    # kwargs = dictionary
    number+=kwargs['add']
    number+=kwargs['multiply']
    return number

print(calculate(10, add =3, multiply = 5))


class Car:
    def __init__(self,**kw):
        self.wheel = 4
        self.make = kw.get("make")
        self.model = kw.get("model")
        # benefit of get in dict, will returns none if there is no arguments

my_car = Car(make = 'Nissan', model = 'GTR')
print(my_car.model)
my_car2 = Car() # if it wasnt specified, it may result in key error
print(my_car2.make)
