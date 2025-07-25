with open("Input/numbers.txt") as file:
    numbers = [int(line.strip()) for line in file]
    max_num = max(numbers)
with open("Output/output09.txt" , "w") as file:
    file.write(f"Eng katta son: {max_num}")    