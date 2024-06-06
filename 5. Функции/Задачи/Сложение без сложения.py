def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    return a
print(sum(2, 2))