from os import system, name
def clear():
  '''Library Way to Clear Screen'''
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def tip_calculator():
  '''Tip Calculator Function'''
  print("Welcome to the tip calculator.")
  try:
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    if tip_percentage not in [10,12,15]:
      raise ValueError("Tip Percentage must be 10, 12, or 15!")
    num_of_people = int(input("How many people to split the bill? "))
  except ValueError as error_message:
    print(error_message)
    input("Press enter to continue...")
    clear()
    tip_calculator()
  else:
    tip = total_bill * (1+(tip_percentage/100))
    print(f'Each person should pay: ${round(tip/num_of_people,2)}')
  
tip_calculator()

# We can actually use looping to validate each input
# Im not doing it since it'll take too much time
