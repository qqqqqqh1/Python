n = int(input())


def is_prime(num):  # 7
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0
number = 1
while count < n:
    if is_prime(number):
        count += 1
        print(number, end=' ')
    number += 1
