nums = list(map(int, input().split()))
n = int(input())
nums = nums[-n:] + nums[:-n]
print(*nums, sep=' ')
