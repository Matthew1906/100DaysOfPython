# For loops, Range, and Code Blocks

# 1. For Loops
fruits = ["Apple", "Peach", "Banana"]
for fruit in fruits:
    print(fruit + " Pie")
# INDENTATION IS IMPORTANT!!

# 2. Range Functions
for num in range(1,10,3):
    # range(x,y,z)
    # x = start from x
    # y = until before y
    # z = size of steps
    print(num)

# Gaussian formula
total = 0
for num in range(1,101):
    total+=num
