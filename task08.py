with open("Input/numbers.txt") as file:
    numbers = [int(line.strip()) for line in file]
    total = sum(numbers)
with open("Output/output08.txt" , "w") as file:
    file.write(f"Yig'indi: {total}")    