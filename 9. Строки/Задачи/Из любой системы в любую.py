def convert(num_10, k, m):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if k == m:
        return num_10

    if num_10 < 0:
        sign = "-"
        num_10 = -num_10
    else:
        sign = ""

    result = ""
    while num_10 > 0:
        result = alpha[num_10 % m] + result
        num_10 //= m

    return sign + result

n = input()
k, m = map(int, input().split())

num_10 = int(n, k)

print(convert(num_10, 10, m))