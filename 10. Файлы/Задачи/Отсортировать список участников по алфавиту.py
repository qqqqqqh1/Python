scores = []

with open('input(2).txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split()
        first_name, last_name, a, score = line
        scores.append((first_name, last_name, int(score)))
    for first_name, last_name, score in sorted(scores):
        print(f'{first_name} {last_name} {score}')
