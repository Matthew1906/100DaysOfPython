# Exercise 5

weather_c = {
    "Monday":12,
    "Tuesday":14,
    'Wednesday':15,
    'Thursday':14,
    'Friday':21,
    'Saturday':22,
    'Sunday':24
}

weather_f = {key:round((9/5*temp_c)+32,2) for (key,temp_c) in weather_c.items()}
print(weather_f)