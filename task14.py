import json
with open("Input/students.json") as file:
    data = json.load(file)
a_names = [s["name"] for s in data if s["name"].startswith("A")]  
with open("Output/output14.json" , "w") as file:
    json.dump({"a_names" : a_names},file)    