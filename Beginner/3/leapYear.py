# EXERCISE 3: LEAP YEAR
year = int(input("Which year do you want to check? "))
leap_year = False
if year%4==0:
    leap_year = True
    if year%100==0:
        leap_year = False
        if year%400==0:
            leap_year = True
if leap_year:
    print("It's a leap year!")
else:
    print("It's not a leap year!")