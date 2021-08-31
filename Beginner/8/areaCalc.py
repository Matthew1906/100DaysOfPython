# EXERCISE 1 = Area Calculator

def areaCalc(height, width):
    # you can also use ceil function by importing math
    area = (width*height)//5
    if (width*height)%5!=0:
        area+=1
    print(f"You'll need {area} can(s) of paint.")

areaCalc(height=int(input("test h = ")), width = int(input("test w = ")))
