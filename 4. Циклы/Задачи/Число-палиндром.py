a = int(input()) #121
tmp = a
re_a = 0

while a != 0:
    re_a = (re_a * 10) + (a % 10)
    a //= 10

print(re_a)

# Альтернативная версия
print('YES' if str(tmp) == str(tmp)[::-1] else 'NO')