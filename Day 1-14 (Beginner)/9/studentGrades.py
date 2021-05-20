# Exercise 1: Student Grades

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
for k,v in student_scores.items():
    grade = ""
    if 91<=v<=100:
        grade = "Outstanding"
    elif 81<=v<=90:
        grade = "Exceeds Expectations"
    elif 71<=v<=80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[k] = grade
print(student_grades)
