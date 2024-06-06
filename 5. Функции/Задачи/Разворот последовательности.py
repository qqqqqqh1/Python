def sef():
    a = int(input())
    if a != 0:
        sef()
        print(a)
print(sef())
