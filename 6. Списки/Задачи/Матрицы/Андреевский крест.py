n = int(input())
matrix = [["1" if i + j == n - 1 or i == j else "0" for j in range(n)] for i in range(n)]
for row in matrix:
    print(*row)
print()
