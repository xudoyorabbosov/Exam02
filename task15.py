import csv

with open ("Input/grades.csv") as f:
    reader = csv.reader(f)
    grades = list(reader)
max_grade = -1
top_student = ""
for name , grade in grades:
    grade = int(grade)
    if grade > max_grade:
        max_grade = grade
        top_student = name 
with open ("Output/output15.txt", "w") as f:
    f.write(f"Bahosi eng yuqori o'quvchi: {top_student} - {max_grade}")            