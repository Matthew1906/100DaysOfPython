# EXERCISE 1: Average Height

student_heights = input("Input a list of student heights! (separated by space)\n").split(" ")
total_height = 0
for student_height in student_heights:
    total_height += int(student_height)
print(round(total_height/len(student_heights)))

# Example testcase:
# 180 124 165 173 169 146 189
# 156 178 165 171 187