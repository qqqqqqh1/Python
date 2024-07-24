res = []
count = 0
alpha = 'abcdefghijklmnopqrstuvwxyz'

with open('input(3).txt', encoding='utf-8') as f:
    line = f.readline()
    for char in line:
        if char == '0':
            count += 1
        elif char == '1':
            res.append(alpha[count])
            count = 0
    print(*res, sep='')
