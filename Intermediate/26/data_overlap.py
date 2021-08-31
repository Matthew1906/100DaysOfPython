# Exercise 3: Data Overlap

def convert_int(num):
    res = 0
    for i in range(len(num)):
        res+= int(num[i])*(10**(len(num)-i-1))
    return res

with open("file1.txt",'r') as file1:
    numbers_1 = list(map(convert_int, file1.read().split("\n")))

with open("file2.txt",'r') as file2:
    numbers_2 = list(map(convert_int, file2.read().split("\n"))) 

result = [num for num in numbers_1 if num in numbers_2]
print(result)