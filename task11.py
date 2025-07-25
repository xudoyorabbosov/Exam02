import json
with open("Input/students.json") as file:
    data = json.load(file)
count = len(data)    
with open("Output/output11.json" , "w") as file:
    json.dump({"count" : count},file)    