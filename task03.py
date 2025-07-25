def calculate_tax(salary):
    return salary * 0.2 if salary > 5_000_000 else salary * 0.13
def calculate_net_salary(salary):
    return salary - calculate_tax(salary)

maosh = 6_000_000
soliq = calculate_tax(maosh)
sof_maosh = calculate_net_salary(maosh)
print("Soliq:", int(soliq))
print("Sof maosh:", int(sof_maosh))
