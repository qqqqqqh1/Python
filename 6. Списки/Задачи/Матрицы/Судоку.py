n = int(input())
sudoku = []
for i in range(n**2):
  a = list(map(int, input().split()))
  sudoku.append(a)

def row_correct(sudoku, n):
  seen = set()
  for col in range(n**2):
    num = sudoku[0][col]
    if num in seen:
      return False
    seen.add(num)
  for i in range(1, n**2 + 1):
    if i not in seen:
      return False
  return True

def col_correct(sudoku, n):
  seen = set()
  for row in range(n**2):
    num = sudoku[row][0]
    if num in seen:
      return False
    seen.add(num)
  for i in range(1, n**2 + 1):
    if i not in seen:
      return False
  return True

def n_correct(sudoku, i, j, n):
  seen = set()
  for row in range(i * n, (i + 1) * n):
    for col in range(j * n, (j + 1) * n):
      num = sudoku[row][col]
      if num in seen:
        return False
      seen.add(num)
  for i in range(1, 1 + n**2):
    if i not in seen:
      return False
  return True
def sudoku_correct(n, sudoku):
  for row in range(n**2):
    if not row_correct(sudoku, n):
      return False

  for col in range(n**2):
    if not col_correct(sudoku, n):
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