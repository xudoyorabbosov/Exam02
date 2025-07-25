import csv
with open("Input/grades.csv") as f:
    reader = csv.reader(f)
    count = sum(1 for  grade in reader  if int(grade) == 5)
with open("Output/output16.txt", 'w') as f:
    f.write(f"5 baho olganlar soni {count}")