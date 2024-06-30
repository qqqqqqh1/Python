from sys import stdin

d = {}

for row in stdin:
    name, scores = row.split()
    d[name] = d.get(name, 0) + int(scores)
# sorted(d.items()) - Сортируем по имени (по умолчанию многомерные списки сортируются по первому значению)
for name, scores in sorted(d.items()):
    print(name, scores)
