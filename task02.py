def deposit (balance,amount):
    return balance + amount
def withdraw(balance,amount):
    return balance - amount if amount <= balance else "Yetarli mablag' yo'q"
def chek_balance (balance):
    return balance

balance = 100000
balance = deposit(balance, 50000)
print("Yangi balans:", balance)