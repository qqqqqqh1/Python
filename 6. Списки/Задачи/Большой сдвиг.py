nums = list(map(int, input().split()))
n = int(input())
print(nums[-n:]+nums[:-n])
