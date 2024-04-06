start_sum = float(input()) #1000
precent = float(input()) #10
target_sum = float(input()) #2000
month_count = 0
while start_sum < target_sum:
    month_count += 1
    start_sum *= (precent / 100) + 1 # 1100
    print(f'{month_count} - {start_sum:0.2f}')
print(f'Кол-во месяцев: {month_count}')
print(f'Итоговая сумма: {start_sum:0.2f}')