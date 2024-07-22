a = input().split()

max_num = 0
max_str = ''

for i in range(len(a) - 1):
    if len(a[i]) > len(a[i+1]):
        max_num = len(a[i])
        max_str = a[i]

print(max_str)
print(max_num)