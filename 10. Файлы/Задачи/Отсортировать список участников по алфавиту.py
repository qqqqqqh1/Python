scores = {}

with open('input(2).txt', encoding= 'utf-8') as f:
    lines = f.readlines()
    for line in lines:
        liness = line.strip().split()
        first_name, last_name, a, score = liness
        scores[(first_name, last_name)] = int(score)
        sorted_scores = sorted(scores.items())
    for (first_name, last_name), score in sorted_scores:
        print(f'{first_name} {last_name} - {score}')