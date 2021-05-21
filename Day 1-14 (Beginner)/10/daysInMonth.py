#Exercise 1: Days in Month

def isLeapYear(year):
    '''check if a year is a leap year'''
    leap_year = False
    if year%4==0:
        leap_year = True
        if year%100==0:
            leap_year = False
            if year%400==0:
                leap_year = True
    return leap_year

def days_in_month(year, month):
    '''Get number of days of a month in a specific year'''
    if month<1 or month>12:
        return "Invalid Month"
    elif year<0:
        return "Invalid Year"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if isLeapYear(year):
        month_days[1] = 29
    return month_days[month-1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)