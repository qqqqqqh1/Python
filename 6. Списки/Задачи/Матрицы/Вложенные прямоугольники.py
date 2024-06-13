rows = int(input())
cols = int(input())
matrix = [[min(i, j, cols - i - 1, rows - j - 1) for i in range(cols)] for j in range(rows)]
for row in matrix:
    for elem in row:
        print(f'{elem:<3d}', end='')
    print()