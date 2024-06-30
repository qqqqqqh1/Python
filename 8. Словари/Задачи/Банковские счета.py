bank = {}

def DEPOSIT(name, sum):
    bank[name] = bank.get(name, 0) + int(sum)

def WITHDRAW(name, sum):
    if bank[name] > 0:bank[name] = bank.get(name, 0) - int(sum)

def BALANCE(name):
    if name in bank:
        print(bank[name])
    else:
        print('ERROR')

def TRANSFER(name1, name2, sum):
    bank[name1] = bank.get(name1) + int(sum)
    bank[name2] = bank.get(name2, 0) - int(sum)

def INCOME(p):
    for key, *value in bank.items():
        for i in range(len(value)):
            for number in value:
                if number > 0:
                    bank[key] = int(number * ((int(p) / 100) + 1))

while True:
    row = input().split()
    if row == '':
        break
    else:
        if 'DEPOSIT' in row:
            DEPOSIT(row[1], row[2])
        elif 'WITHDRAW' in row:
            WITHDRAW(row[1], row[2])
        elif 'BALANCE' in row:
            BALANCE(row[1])
        elif 'TRANSFER' in row:
            TRANSFER(row[1], row[2], row[3])
        elif 'INCOME' in row:
            INCOME(row[1])