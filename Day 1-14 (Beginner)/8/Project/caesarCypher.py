# DAY 8 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: CAESAR CYPHER
# THINGS I LEARNT: caesar cypher, ascii manipulation, modulus operator, functions
from art import logo

# There is a slight difference since i manipulate the ascii value, while in the course it uses simple addition
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

print(logo)
while True:
    direction = input("Type 'encode' to encypt, type 'decode' to decrypt:\n")
    # convert to list so that it can be manipulated
    text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    caesar(string = text, direction=direction, shift = shift)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if again =='no':
        break