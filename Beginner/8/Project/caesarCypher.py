from art import logo
from os import system, name

def clear():
  '''Library Way to Clear Screen'''
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def caesar(string, shift, direction):
    for i in range(len(string)):
        # check if its an alphabet
        if not string[i].isalpha():
            continue
        # use ascii manipulation (ord() to convert to ascii value and chr() to convert to string)
        if direction=='encode':
            value = (ord(string[i])-ord('a')+shift)
        else:
            value = (ord(string[i])-ord('a')-shift)
        # use modulus just in case the shift is too large
        value%=25
        string[i] = chr(value+ord('a'))
    string = "".join(string)
    if direction == 'encode':
        print(f"Here's the encoded result {string}")
    else: 
        print(f"Here's the decoded result {string}")

while True:
    print(logo)
    direction = input("Type 'encode' to encypt, type 'decode' to decrypt:\n")
    # convert to list so that it can be manipulated
    text = list(input("Type your message:\n").lower())
    try:
      shift = int(input("Type the shift number:\n"))
    except ValueError as error_message:
      print(error_message)
      input("Press enter to restart...")
      clear()
      continue
    else:
      caesar(string = text, direction=direction, shift = shift)
      again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
      if again =='no':
          break