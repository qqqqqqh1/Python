z = zip([5,3,6,7], [1,2,3,5], [7,8,96,2])
for i in z:
    print(i)
def f(a, b, c):
    print(a+b+c)

args = (('b', 2),('a', 1),('c', 3))

f(**dict(args))