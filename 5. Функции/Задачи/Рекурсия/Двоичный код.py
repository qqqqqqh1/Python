n = int(input()) #136

def to_bin(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + str(binary)  # 0
        n //= 2 # 68
    return binary

print(to_bin(n))