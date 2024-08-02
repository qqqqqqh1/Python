from itertools import permutations

table = "15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"
graph = "АБ БА АГ ГА ЕГ ГЕ ЕЖ ЖЕ ВД ДВ ДЖ ЖД ЖИ ИЖ ВИ ИВ ГБ БГ АЕ ЕА БВ ВБ"

print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕЖИ'):
    for d in ['ГД ДГ', 'ГИ ИГ', 'ДБ БД', 'ИБ БИ', 'АД ДА']:
        new_graph = graph + f' {d}'
        new_table = table
        for i in range(1, 9):
            new_table = new_table.replace(str(i), p[i - 1])
        if set(new_table.split()) == set(new_graph.split()):
            print(*p)
            print(d)
            print()
