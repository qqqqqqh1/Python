total_sum = 0
i = 0
with open('input.txt') as f:
    for line in f:
        s = sum(list(map(int, line.split())))
        total_sum += s
        print(f'Строка {(i := i + 1)} - {s}')
    print(f'Общая сумма: {total_sum}')