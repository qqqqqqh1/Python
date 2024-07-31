from itertools import permutations

table = "14 15 23 24 25 32 35 36 41 42 47 51 52 53 63 67 74 76"
graph = "BD BF BC DC DB DE EA ED AE AG GA GC GF CD CB CG FB FG"

print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    new_graph = table
    for i in range(1, 8):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*p)
