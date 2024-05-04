def to_bin(n):
    if n > 0:
        return to_bin(n // 2) + str(n % 2)
    return ''


print(to_bin(int(input())))
