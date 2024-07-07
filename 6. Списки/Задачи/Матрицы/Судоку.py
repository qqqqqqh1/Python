n = int(input())
sudoku = []
for i in range(n ** 2):
    a = list(map(int, input().split()))
    sudoku.append(a)


def row_correct(sudoku, row, n):
    return set(range(1, n ** 2 + 1)).symmetric_difference(set(sudoku[row])) == set()


def col_correct(sudoku, col, n):
    seen = set()
    for row in range(n ** 2):
        seen.add(sudoku[col][row])
    return set(range(1, n ** 2 + 1)).symmetric_difference(seen) == set()


def n_correct(sudoku, i, j, n):
    seen = set()
    for row in range(i * n, (i + 1) * n):
        for col in range(j * n, (j + 1) * n):
            num = sudoku[row][col]
            if num in seen:
                return False
            seen.add(num)
    return set(range(1, n ** 2 + 1)).symmetric_difference(seen) == set()


def sudoku_correct(n, sudoku):
    for row in range(n ** 2):
        if not row_correct(sudoku, row, n):
            return False

    for col in range(n ** 2):
        if not col_correct(sudoku, col, n):
            return False

    for i in range(n):
        for j in range(n):
            if not n_correct(sudoku, i, j, n):
                return False
    return True


if sudoku_correct(n, sudoku):
    print('Correct')
else:
    print('Incorrect')
