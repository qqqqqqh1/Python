def f(num):
    b = bin(num)[2:] + bin(num % 4)[2:]
    return int(b, 2)


count = 0
for i in range(1_000_000_000, 1_789_456_123 + 1):
    if i % 2 == 0 or i % 4 == 0:
        count += 1
print(count)
