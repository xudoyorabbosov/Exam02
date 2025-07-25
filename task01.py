def add(a, b):
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b if b != 0 else "Bo'lish mumkin emas"

a = 8
b = 5
action = "*"

if action == '+':
    print("Natija:", add(a,b))
elif action == '-':
    print("Natija:", subtract(a,b))    
elif action == '*':
    print("Natija:", multiply(a,b))
elif action == '/':
    print("Natija:", divide(a,b))        