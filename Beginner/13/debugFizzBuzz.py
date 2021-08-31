for number in range(1, 101):
    # use and instead of or
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
    # use elif instead of if
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)