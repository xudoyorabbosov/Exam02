import json
with open("Input/students.json") as file:
    data = json.load(file)
names = sorted(student["name"] for student in data)    
with open("Output/output12.json" , "w") as file:
    json.dump({"Sorted names" : names},file)    