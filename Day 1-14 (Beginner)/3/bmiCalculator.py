# EXERCISE 2: BMI calculator 2.0
weight = float(input("Input your weight in kg: "))
height = float(input("Input your height in m: "))
body_mass_index = weight/height**2
if body_mass_index<18.5:
    print(f"Your Body Mass Index is {body_mass_index}, you are underweight!")
elif body_mass_index<25:
    print(f"Your Body Mass Index is {body_mass_index}, You have a normal weight!")
elif body_mass_index<30:
    print(f"Your Body Mass Index is {body_mass_index}, You are overweight!")
elif body_mass_index<35:
    print(f"Your Body Mass Index is {body_mass_index}, You are obese!")
else:
    print(f"Your Body Mass Index is {body_mass_index}, You are clinically obese!")