m = dict()
for i in range(int(input())):
    key, *values = input().split()
    for value in values:
        m[value] = key
print(*(m[input()] for i in range(int(input()))), sep='\n')
