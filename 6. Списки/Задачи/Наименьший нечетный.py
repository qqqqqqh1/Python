nums = list(map(int, input().split()))
print(min(nums, key=lambda x: x if x % 2!=0 and x >= 1 else 0))