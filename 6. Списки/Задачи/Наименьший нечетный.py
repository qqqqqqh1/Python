nums = list(map(int, input().split()))
min_num = max(nums)
for num in nums:
    if num < min_num and num % 2 != 0:
        min_num = num

if min_num % 2 == 0:
    print(0)
else:
    print(min_num)