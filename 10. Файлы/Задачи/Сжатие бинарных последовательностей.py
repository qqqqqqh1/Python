res = []
count = 0
rs = ''
alpha = 'abcdefghijklmnopqrstuvwxyz'

with open('input(3).txt', encoding = 'utf-8') as f:
    line = f.readline()
    for char in line:
        if char == '0':
            count += 1
        elif char == '1':
            rs = alpha[count]
            res.append(rs)
            count = 0
    print(*res, sep ='')