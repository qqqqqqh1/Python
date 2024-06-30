from sys import stdin

bank = {}


def DEPOSIT(name, sum):
    bank[name] = bank.get(name, 0) + sum


def WITHDRAW(name, sum):
    if bank[name] > 0:
        bank[name] = bank.get(name, 0) - sum


def BALANCE(name):
    if name in bank:
        print(bank[name])
    else:
        print('ERROR')


def TRANSFER(name1, name2, sum):
    bank[name1] = bank.get(name1) - sum
    bank[name2] = bank.get(name2, 0) + sum


def INCOME(p):
    for key, value in bank.items():
        if value > 0:
            bank[key] = int(int(value) * ((p / 100) + 1))


for line in stdin:
    row = line.split()
    if 'DEPOSIT' in row:
        DEPOSIT(row[1], int(row[2]))
    elif 'WITHDRAW' in row:
        WITHDRAW(row[1], int(row[2]))
    elif 'BALANCE' in row:
        BALANCE(row[1])
    elif 'TRANSFER' in row:
        TRANSFER(row[1], row[2], int(row[3]))
    elif 'INCOME' in row:
        INCOME(int(row[1]))
