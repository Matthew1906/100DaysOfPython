# EXERCISE 4 : Fizz Buzz Challenge -> used in interview questions

for num in range(1,101):
    res = ""
    if num%3==0:
        res+="Fizz"
    if num%5==0:
        res+="Buzz"
    if res=="":
        print(num)
    else:
        print(res)
