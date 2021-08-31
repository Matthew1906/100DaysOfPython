import datetime as dt

now = dt.datetime.now() #current date and time
print(now)
print(now.year)
print(now.weekday())

# Create Date time of my own

date_of_birth = dt.datetime(year = 2000, month=10, day= 12)
print(date_of_birth)