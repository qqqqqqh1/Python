rows = int(input())
cols = int(input())
matrix = [[i * j for j in range(cols)] for i in range(rows)]
for row in matrix:
    for elem in row:
        print(f'{elem:<3d}', end='')
    print()
