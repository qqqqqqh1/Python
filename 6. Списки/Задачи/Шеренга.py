nums = list(map(int, input().split()))
num = int(input())
pos = 1
for position in nums:
    if position >= num:
        pos += 1
print(pos)