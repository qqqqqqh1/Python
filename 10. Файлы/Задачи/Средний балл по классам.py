scores = {9: [], 10: [], 11: []}

with open('input(1).txt', encoding='utf-8') as f:
    for line in f:
        liness = line.strip().split()
        first_name, last_name, rank, score = liness
        rank, score = float(rank), float(score)

        if rank in scores:
            scores[rank].append(score)

average_score = {}

for rank, estimation in scores.items():
    average_score[rank] = sum(estimation) / len(estimation)

for a, b in average_score.items():
    print(f'У {a} класса средняя оценка {b}')