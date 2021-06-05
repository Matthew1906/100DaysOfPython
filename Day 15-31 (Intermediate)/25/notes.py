# 1. Using CSV module
# import csv
# day = []
# temperatures = []
# weather = []
# with open("weather_data.csv") as weather_file:
#     weather_data = list(csv.reader(weather_file))
#     for row in range(1,len(weather_data)):
#         day.append(weather_data[row][0])
#         temperatures.append(int(weather_data[row][1]))
#         weather.append(weather_data[row][2])

# 2. Using Pandas module
# Powerful Data Analysis Library
import pandas as pd
weather_df = pd.read_csv("weather_data.csv")

# The Table is called as Dataframe
# A single column is called as series

# finding a column
print(weather_df['condition'])

# We can also use it like accessing attribute in an object
print(weather_df.condition)

# Conversion example
weather_dict = weather_df.to_dict()

# Convert a series to a list
temp_list = weather_df['temp'].to_list()

# Find Average Temperature -> mean
print(weather_df['temp'].mean())
# Find Max Temperature -> max
print(weather_df['temp'].max())
# Find Min Temperature -> min
print(weather_df['temp'].min())

# Get an entire row
print(weather_df[weather_df["day"] == 'Monday'])

# Get the rows where temperature is at maximum
print(weather_df[weather_df["temp"] == weather_df['temp'].max()])

# Get the column of a specific row
print(weather_df[weather_df["temp"] == weather_df['temp'].max()]['condition'])

# Get Monday's temperature in Fahrenheit
monday_temp = int(weather_df[weather_df["day"] == 'Monday']['temp'])
print(((9*(monday_temp)/5)+32))

# Create Dataframe
data = [
    {
        "name":"Martin",
        "age":12
    },
    {
        "name":"Kevin",
        "age":18
    },
    {
        "name":"Hitch",
        "age":16
    }
]
    
student_df = pd.DataFrame(data)
student_df.to_csv("student_data.csv")