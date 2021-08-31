# EXERCISE 2: High Score

student_scores = input("Input a list of student scores! (separated by space)\n").split(" ")
highest = 0
for student_score in student_scores:
    if int(student_score)>highest:
        highest = int(student_score)
print(f"The highest score in this class is: {highest}")

# Testcases:
# 78 65 89 86 55 91 64 89