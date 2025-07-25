students = {'Ali': 5, 'Vali': 4, 'Husan': 5, 'Husan': 3}
result = sum(students.values()) / len(students)
above = [name for name, grade in students.items() if grade > result]
print("O'rtacha baho :" ,result)
print(f"{result} dan yuqori:", ",".join(above))