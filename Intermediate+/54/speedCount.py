# Day 54 Exercise of 100 Days of Python
# Exercise Name: Speed Count (There is no name so i just made sth up)
# Things i implemented: Time, Decorator

import time

def speed_calc_decorator(function):
    def calc_speed():
        begin = time.time()
        function()
        end = time.time()
        print(f'{function.__name__} run speed: {end-begin} s.')
    return calc_speed

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i
        
fast_function()
slow_function()