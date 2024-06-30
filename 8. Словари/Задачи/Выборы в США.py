d = {}

while True:
    row = input()
    if row == '':
        break
    else:
        name, scores = row.split()
        d[name] = d.get(name, 0) + int(scores)
for name, scores in sorted(d.items()):
    print(name, scores)