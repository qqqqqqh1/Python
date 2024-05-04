n = int(input())
def is_perfect_number(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += i
    return count == num

count = 0
num = 1
while count < n:
    if is_perfect_number(num):
        count += 1
        print(num, end=' ')
    num += 1
