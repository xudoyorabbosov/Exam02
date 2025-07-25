with open("Input/numbers.txt") as file:
    numbers = sorted(int(line.strip()) for line in file)
with open("Output/output10.txt" , "w") as file:
    for  num in numbers:
        file.write(f" {num}/n")    