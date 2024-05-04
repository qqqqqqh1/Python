def to_bin(n):
    if n > 0:
        binary = ''
        binary += str(n % 2) + binary
        return binary + to_bin(n//2)
    else:
        return ''
print(to_bin(int(input()))[::-1])