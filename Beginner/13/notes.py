############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
    # won't print anything because it stops at 20
    # fix = change the range to 1,21
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num-1])
# wrong in index, you can change the range of randint to 0,5
# or print dice_imgs[dice_num-1]

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")
# Must include 1994 to be a Gen Z
# >= 1994
# already fixed it too

# # Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print("You can drive at age {age}.")
# indentation error -> already fixed it so that its clear
# type error too

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
# error => ==, should be =, already fixed it
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
      new_item = item * 2
      b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])