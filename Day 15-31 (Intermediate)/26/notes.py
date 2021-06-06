# List Comprehension

# Unique to python

# Normal assignment using for loop
number = []
for i in range(1,5):
    number.append(i)
print(number)

# using list comprehension
number = [i*2 for i in range(1,5)]
print(number)

name = "Matthew"
name_list = [letter for letter in name]
print(name_list)

# Use conditions in list comprehension

names = ['alex', 'beth', 'caroline','dave', 'eleanor','freddie']
names = [name.capitalize() for name in names]

shortened_names = [name for name in names if len(name)<=4]
print(shortened_names)

upper_long_names = [name.upper() for name in names if len(name)>=5]
print(upper_long_names)


# Dictionary comprehension
from random import randint
student_scores = {key:randint(1,100) for key in names}
print(student_scores)
student_passed = {key:value for (key,value)in student_scores.items() if value>=75}
print(student_passed)

# Iterate through a pandas dataframe

import pandas as pd

student_dict = {
    'student':['angela','james','lily'],
    'score':[56,78,98]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

for key,value in student_df.items():
    print(key)