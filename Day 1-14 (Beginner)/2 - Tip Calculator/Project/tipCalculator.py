# DAY 2 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: TIP CALCULATOR
# THINGS I LEARNT: DATA TYPES, TYPE CASTING, NUMERICAL OPERATORS, F-STRING

print("Welcome to the tip calculator.")
# Since try catch hasn't been taught yet, will assume the input is correct
total_bill = float(input("What was the total bill? $"))
# Since if else also hasn't been taught yet, will assume the tip percentage input is always within the scope
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
tip = total_bill * (1+(tip_percentage/100))
# use f-strings to make it easier to print
print(f'Each person should pay: ${round(tip/num_of_people,2)}')
