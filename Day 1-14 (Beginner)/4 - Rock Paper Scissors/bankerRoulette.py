import random

friends = input("Give me everybody's names, separated by comma!\n").split(",")

res = random.randint(0,len(friends)-1)

payer = friends[res].strip()

print(f'{payer} is going to buy the meal today!')

# we can also use choice function
