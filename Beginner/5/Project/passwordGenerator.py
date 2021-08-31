from os import system, name

def clear():
  '''Library Way to Clear Screen'''
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

# import random module
import random

# List all numbers, alphabets, symbols
letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
numbers = "0 1 2 3 4 5 6 7 8 9".split(" ")
symbols = "! # $ % & ( ) * +".split(" ")

def password_generator():
  # Prompt
  print("Welcome to the PyPassword Generator!")
  try:
    letter_amount = int(input("How many letters would you like in your password?\n"))
    symbol_amount = int(input("How many symbols would you like?\n"))
    number_amount = int(input("How many numbers would you like?\n"))
  except ValueError as error_message:
    print(error_message)
    input("Press enter to continue...")
    clear()
    password_generator()
  else:
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
    if input("Type y to generate new password: ")=='y':
      clear()
      password_generator()
password_generator()