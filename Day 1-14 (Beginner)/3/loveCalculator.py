name = input("Enter your name: ").upper()
match_name = input("Enter their name: ").upper()

combi = name+match_name

trueCalc = combi.count("T") + combi.count("R") + combi.count("U") + combi.count("E")
loveCalc = combi.count("L") + combi.count("O") + combi.count("V") + combi.count("E")

score = trueCalc*10 + loveCalc

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
