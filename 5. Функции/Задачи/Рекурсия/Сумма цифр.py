def sum_digits(num):
    if num > 0:
        return (num % 10) + sum_digits(num // 10)
    return 0


print(sum_digits(int(input())))
