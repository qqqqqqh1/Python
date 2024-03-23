a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and c + a > b:
    h = max(a, b, c)
    c1 = min(a, b, c)
    c2 = (a + b + c) - (h + c1)
    if h ** 2 < c1 ** 2 + c2 ** 2:
        print('остроугольный')
    elif h ** 2 == c1 ** 2 + c2 ** 2:
        print('прямоугольный')
    else:
        print('тупоугольный')
else:
    print('impossible')