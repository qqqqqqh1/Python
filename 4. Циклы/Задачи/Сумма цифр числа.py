a = int(input())  # 123
sum_nums = 0

while a != 0:
    sum_nums += a % 10
    a //= 10
print(sum_nums)

# Альтернативная версия
print(sum(map(int, list(str(1234)))))