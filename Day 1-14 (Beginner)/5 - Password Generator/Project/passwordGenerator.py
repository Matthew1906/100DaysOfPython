# DAY 5 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: PASSWORD GENERATOR
# THINGS I LEARNT: RANDOM, FOR LOOPS, LISTS, HOW TO MAKE INFINITE LOOP WITH FOR LOOPS (FROM INTERNET)

# import random module
import random

# List all numbers, alphabets, symbols
letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")
symbols = "! # $ % & ( ) * +".split(" ")

# Prompt
print("Welcome to the PyPassword Generator!")
letter_amount = int(input("How many letters would you like in your password?\n"))
symbol_amount = int(input("How many symbols would you like?\n"))
number_amount = int(input("How many numbers would you like?\n"))

# TO USE THIS CODE, YOU CAN CHOOSE ONE OF THESE CODES
# IF YOU DON'T COMMENT THE ONE OF THEM, THEN THE PROGRAM WILL GENERATE 2 PASSWORDS
# COMMENT THE OTHERS BY BLOCKING THEM, AND CTRL + /

# A. Generate Password -> THE COMPLICATED WAY
# INSERT EACH ELEMENT, AND RANDOMIZE THE INDEX
# COMPLICATED BECAUSE IT REQUIRES INFINITE LOOPS AND MULTIPLE LISTS
password_length = letter_amount+symbol_amount+number_amount
password = ["_"]*password_length
used_index = [False]*password_length
for i in range(letter_amount):
    letter = letters[random.randint(1,len(letters)-1)]
    # INFINITE LOOPING
    infinite_loop = [1]
    for j in infinite_loop:
        index = random.randint(0,password_length-1)
        # check if the index is already occupied
        if not used_index[index]:
            used_index[index] = True
            password[index] = letter
            break
        infinite_loop.append(j+1)
for i in range(symbol_amount):
    symbol = symbols[random.randint(1,len(symbols)-1)]
    # INFINITE LOOPING
    infinite_loop = [1]
    for j in infinite_loop:
        index = random.randint(0,password_length-1)
        # check if the index is already occupied
        if not used_index[index]:
            used_index[index] = True
            password[index] = symbol
            break
        infinite_loop.append(j+1)
for i in range(number_amount):
    number = numbers[random.randint(1,len(numbers)-1)]
    # INFINITE LOOPING
    infinite_loop = [1]
    for j in infinite_loop:
        index = random.randint(0,password_length-1)
        # check if the index is already occupied
        if not used_index[index]:
            used_index[index] = True
            password[index] = number
            break
        infinite_loop.append(j+1)
print("Your Password is "+"".join(password))


# B. GENERATE PASSWORD -> THE SIMPLER WAY
# ONLY NEED TO INSERT RANDOM LETTERS, SYMBOLS, NUMBERS INTO THE LIST
# SHUFFLE THEM USING A FUNCTION FROM THE RANDOM MODULE
# THIS IS THE COURSE'S WAY
password = []
for i in range(letter_amount):
    letter = letters[random.randint(1,len(letters)-1)]
    password.append(letter)
for i in range(symbol_amount):
    symbol = symbols[random.randint(1,len(symbols)-1)]
    password.append(symbol)
for i in range(number_amount):
    number = numbers[random.randint(1,len(numbers)-1)]
    password.append(number)
# shuffling function
random.shuffle(password)
print("Your Password is "+"".join(password))