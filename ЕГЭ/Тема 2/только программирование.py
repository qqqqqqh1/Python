from itertools import product, permutations


def f(x, y, z):
    return (x == z) or (x <= (y and z))

# x1 ... xn; n = Кол-во неизвестных ячеек в таблице
for x1, x2, x3 in product([0, 1], repeat=3):
    table = [
        (0, 0, x1, 0),
        (1, x2, x3, 0)
    ]
    # Проверка на уникальность строк
    if len(table) == len(set(table)):
        for p in permutations('xyz'):
            if all(f(**dict(zip(p, s))) == s[-1] for s in table):
                print(p)
