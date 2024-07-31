N, M, K = map(int, input().split())
matrix = [['.' for i in range(M)] for j in range(N)]
for i in range(K):
    r, t = map(int, input().split())
    matrix[r - 1][t - 1] = '*'
for i in range(N):
    for j in range(M):
        count = 0
        for row in range(max(0, i - 1), min(N, i + 2)):
            for col in range(max(0, j - 1), min(M, j + 2)):
                if matrix[row][col] == '*':
                    count += 1
        if count > 0 and matrix[i][j] != '*':
            matrix[i][j] = str(count)
print(*matrix, sep='\n')