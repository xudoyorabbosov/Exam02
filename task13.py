import json
with open("Input/students.json") as file:
    data = json.load(file)
long_names = [student["name"] for student in data if len(student["name"]) > 5]   
with open("Output/output13.json" , "w") as file:
    json.dump({"long names" : long_names},file)    